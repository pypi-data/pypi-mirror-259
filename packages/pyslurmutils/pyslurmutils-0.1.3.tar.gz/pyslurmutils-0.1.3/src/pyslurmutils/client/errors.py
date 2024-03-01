import importlib
from typing import List, Type, Tuple
import tblib


class SlurmError(Exception):
    pass


class SlurmHttpError(SlurmError):
    pass


def raise_chained_errors(
    errors: List[str], exc_class: Type[Exception] = SlurmHttpError
):
    try:
        if len(errors) > 1:
            raise_chained_errors(errors[:-1], exc_class=exc_class)
    except exc_class as e:
        raise exc_class(errors[-1]) from e
    else:
        raise exc_class(errors[-1])


class RemoteSlurmException(SlurmError):
    pass


def remote_exception_from_tb(exc_info: List[Tuple[str, str, str, bool]]) -> Exception:
    if not exc_info:
        raise ValueError("No exception information provided")
    exc_top = None
    exc_prev = None
    for exc_class_string, exc_message, exc_tb_string, cause in exc_info:
        exc = _exception_from_tb(exc_class_string, exc_message, exc_tb_string)
        if exc_top is None:
            exc_top = exc
            assert cause is None
        else:
            if cause:
                exc_prev.__cause__ = exc
            else:
                exc_prev.__context__ = exc
        exc_prev = exc
    return exc_top


def _exception_from_tb(
    exc_class_string: str, exc_message: str, exc_tb_string: str
) -> Exception:
    module_name, _, class_name = exc_class_string.rpartition(".")

    try:
        mod = importlib.import_module(module_name)
        exc_class = getattr(mod, class_name)
    except (ImportError, AttributeError):
        exc = RemoteSlurmException(exc_message)
    else:
        try:
            exc = exc_class(exc_message)
        except Exception:
            exc = RemoteSlurmException(exc_message)

    tb = tblib.Traceback.from_string(exc_tb_string).as_traceback()

    return exc.with_traceback(tb)


def reraise_remote_exception_from_tb(
    exc_info: List[Tuple[str, str, str, bool]]
) -> None:
    raise remote_exception_from_tb(exc_info)
