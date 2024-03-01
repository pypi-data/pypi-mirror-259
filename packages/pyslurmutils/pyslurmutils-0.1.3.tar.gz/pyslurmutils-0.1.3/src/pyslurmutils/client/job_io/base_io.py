"""Base classes for IO to/from SLURM python jobs
"""

import logging
from contextlib import contextmanager
from numbers import Number
from typing import Any, List, Optional, Tuple
from weakref import proxy
from weakref import WeakValueDictionary
from concurrent import futures

logger = logging.getLogger(__name__)


class Future:
    """Mimic `concurrent.futures` API"""

    def __init__(self, job_id: int, client=None) -> None:
        self.job_id = job_id
        self._client = client

    def __repr__(self):
        return f"{type(self).__name__}({self.job_id})"

    def cancel(self) -> bool:
        """Cancel the future if possible. The SLURM job is not affected.

        Returns True if the future was cancelled, False otherwise. A future
        cannot be cancelled if it is running or has already completed.
        """
        raise NotImplementedError

    def result(self, timeout: Optional[Number] = None) -> Any:
        """Waits for the result indefinitely by default.

        :raises:
            CancelledError: If the future was cancelled.
            TimeoutError: If the future didn't finish executing before the given
                timeout.
            Exception: the exception raised by the job
        """
        raise NotImplementedError

    def exception(self, timeout: Optional[Number] = None) -> Optional[Exception]:
        """Waits for the result indefinitely by default.

        :raises:
            CancelledError: If the future was cancelled.
            TimeoutError: If the future didn't finish executing before the given
                timeout.
        """
        raise NotImplementedError

    def done(self) -> Optional[bool]:
        """Return True if the future was cancelled or finished executing."""
        raise NotImplementedError

    def cancelled(self) -> Optional[bool]:
        """Return True if the future was cancelled."""
        raise NotImplementedError

    def running(self) -> Optional[bool]:
        """Return True if the future is currently executing."""
        raise NotImplementedError

    def wait(self, timeout: Optional[Number] = None) -> bool:
        try:
            self.exception(timeout=timeout)
        except futures.TimeoutError:
            return False
        except futures.CancelledError:
            return True
        return True

    @property
    def client(self):
        return self._client

    def cancel_job(self) -> None:
        """Cancel the SLURM job"""
        try:
            if self._client is None:
                return None
            return self._client.cancel_job(self.job_id)
        except ReferenceError:
            pass

    def cleanup_job(self) -> None:
        """Cleanup job artifacts"""
        try:
            if self._client is None:
                return None
            return self._client.clean_job_artifacts(self.job_id)
        except ReferenceError:
            pass

    def job_status(self) -> None:
        try:
            if self._client is None:
                return None
            return self._client.get_status(self.job_id)
        except ReferenceError:
            pass


class JobIoHandler:
    def __init__(self, client=None) -> None:
        if client is None:
            self._client = None
        else:
            self._client = proxy(client)
        self._futures = WeakValueDictionary()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shutdown(wait=True)
        return False

    def get_future(self, job_id: int) -> Optional[Future]:
        return self._futures.get(job_id, None)

    @contextmanager
    def start_job_io(
        self, data: Any, timeout: Optional[Number] = None
    ) -> Tuple[str, dict, Future]:
        """Returns the script, environment variables and pending result parameters"""
        raise NotImplementedError

    def _finalize_start_job_io(self, future: Future):
        if future.job_id < 0:
            future.cancel()
            return
        self._futures[future.job_id] = future

    def shutdown(self, wait: bool = True, cancel_futures: bool = False) -> None:
        logger.debug("Shutdown %s ...", type(self).__name__)
        for future in list(self._futures.values()):
            if cancel_futures:
                future.cancel()
            elif wait:
                try:
                    future.exception()
                except futures.CancelledError:
                    pass
        logger.debug("Shutdown %s finished", type(self).__name__)

    def get_job_ids(self) -> List[str]:
        """Only the jobs with active futures"""
        return list(self._futures)

    def worker_count(self):
        raise NotImplementedError

    @classmethod
    def _remote_script(cls) -> str:
        return cls._PYTHON_SCRIPT_HEADER + cls._PYTHON_SCRIPT_MAIN

    _PYTHON_SCRIPT_MAIN = NotImplemented

    _PYTHON_SCRIPT_HEADER = """
import os,sys,traceback
print("Python version: %s" % sys.version)
print("working directory: %s" % os.getcwd())

def serialize_exception(exc):
    chain = list()
    cause = None
    while exc:
        if exc.__cause__ is not None:
            next_cause = True
            chained_exc = exc.__cause__
        elif exc.__context__ is not None and not exc.__suppress_context__:
            next_cause = False
            chained_exc = exc.__context__
        else:
            next_cause = None
            chained_exc = None

        exc_class = type(exc)
        exc_class_string = f"{exc_class.__module__}.{exc_class.__name__}"
        exc_tb_string = "".join(
            traceback.format_exception(exc_class, exc, exc.__traceback__, chain=False)
        )

        chain.append((exc_class_string, str(exc), exc_tb_string, cause))
        exc = chained_exc
        cause = next_cause
    return chain
"""
