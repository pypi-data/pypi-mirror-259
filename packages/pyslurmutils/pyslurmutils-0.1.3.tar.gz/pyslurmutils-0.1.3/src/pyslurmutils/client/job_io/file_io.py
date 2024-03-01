"""IO to/from SLURM python jobs over file
"""

import os
import logging
import time
from contextlib import contextmanager
from numbers import Number
from typing import Any, Optional, Tuple
import pickle
from concurrent import futures

from . import base_io
from .. import os_utils
from .. import errors

logger = logging.getLogger(__name__)


class Future(base_io.Future):
    def __init__(self, job_id: int, filename: str, client=None) -> None:
        super().__init__(job_id, client=client)
        self._filename = filename
        self._cancelled = None
        self._finished = None
        self._result = None
        self._tb_info = None

    def __repr__(self):
        return f"Future({self.job_id}, {self._filename})"

    def done(self) -> Optional[bool]:
        if self._cancelled is None and self._finished is None:
            return None
        return self._cancelled or self._finished

    def cancelled(self) -> Optional[bool]:
        return self._cancelled

    def running(self) -> Optional[bool]:
        return self._finished

    def cancel(self) -> bool:
        if self._finished:
            return False
        self._cancelled = True
        return True

    def _fetch(self, timeout: Optional[Number] = None) -> None:
        """
        :raises:
            TimeoutError: the job is not finished
            CancelledError: the job IO was cancelled
        """
        if self._finished:
            return
        t0 = time.time()
        filename = self._filename.replace("%j", str(self.job_id))
        dirname = os.path.dirname(filename)
        if not dirname:
            dirname = "."
        nunpicklingerrors = 0
        while True:
            if self._cancelled:
                raise futures.CancelledError
            try:
                with open(filename, "rb") as f:
                    self._result, self._tb_info = pickle.load(f)
                    self._finished = True
                    return
            except FileNotFoundError:
                try:
                    os.listdir(dirname)  # clear filesystem cache (NFS has this issue)
                except FileNotFoundError:
                    pass
            except pickle.UnpicklingError:
                nunpicklingerrors += 1
                if nunpicklingerrors > 2:
                    raise
            if timeout is not None and (time.time() - t0) > timeout:
                raise futures.TimeoutError
            time.sleep(0.5)

    def result(self, timeout: Optional[Number] = None) -> Any:
        self._fetch(timeout=timeout)
        if self._tb_info:
            errors.reraise_remote_exception_from_tb(self._tb_info)
        return self._result

    def exception(self, timeout: Optional[Number] = None) -> Optional[Exception]:
        self._fetch(timeout=timeout)
        if self._tb_info:
            return errors.remote_exception_from_tb(self._tb_info)


class JobFileIoHandler(base_io.JobIoHandler):
    @contextmanager
    def start_job_io(
        self, data: Any, infile: str, outfile: str
    ) -> Tuple[str, dict, Future]:
        os_utils.makedirs(os.path.dirname(infile))
        os_utils.makedirs(os.path.dirname(outfile))
        with open(infile, "wb") as f:
            pickle.dump(data, f)
        os_utils.chmod(infile)
        environment = {"_PYSLURMUTILS_INFILE": infile, "_PYSLURMUTILS_OUTFILE": outfile}
        future = Future(job_id=-1, filename=outfile, client=self._client)
        try:
            yield self._remote_script(), environment, future
        finally:
            self._finalize_start_job_io(future)

    def worker_count(self):
        return 0

    _PYTHON_SCRIPT_MAIN = """
import pickle

infile = os.environ.get("_PYSLURMUTILS_INFILE")
try:
    outfile = os.environ.get("_PYSLURMUTILS_OUTFILE")
    outfile = outfile.replace("%j", os.environ["SLURM_JOB_ID"])

    try:
        print("Reading function and arguments from", infile)
        with open(infile, "rb") as f:
            func,args,kw = pickle.load(f)

        print("Executing function:", func)
        print("Arguments:", args)
        print("Keyword arguments:", kw)
        if args is None:
            args = tuple()
        if kw is None:
            kw = dict()
        result = func(*args, **kw)
        exc_info = None
    except Exception as e:
        traceback.print_exc()
        result = None
        exc_info = serialize_exception(e)

    os.umask(0)
    os.makedirs(os.path.dirname(outfile), mode=0o777, exist_ok=True)
    with open(outfile, "wb") as f:
        pickle.dump((result, exc_info), f)
    os.chmod(outfile, mode=0o777)
finally:
    if infile:
        os.remove(infile)
"""
