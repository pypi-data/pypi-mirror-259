import gc
import socket
from contextlib import contextmanager, ExitStack
from concurrent.futures import CancelledError
from concurrent.futures import TimeoutError

import pytest

from ..client.job_io import tcp_io


def test_tcp_io():
    with tcp_io.JobTcpIoHandler() as handler:
        with handler.start_job_io({"question"}) as (script, env, future):
            future.job_id = 1234
        with pytest.raises(TimeoutError):
            future.result(timeout=0)
        assert tcp_io.job_test_client(env, ({"response"}, None)) == {"question"}
        assert future.result() == {"response"}


def test_tcp_io_cancel():
    with tcp_io.JobTcpIoHandler() as handler:
        with handler.start_job_io({"question"}) as (script, env, future):
            future.job_id = 1
        future.cancel()
        with pytest.raises(CancelledError):
            future.result()

        with handler.start_job_io({"question"}) as (script, env, future):
            future.job_id = 2
        assert tcp_io.job_test_client(env) == {"question"}
        future.cancel()
        with pytest.raises(CancelledError):
            future.result()


def test_tcp_io_cleanup():
    with tcp_io.JobTcpIoHandler() as handler:
        with handler.start_job_io({"question"}) as (script, env, future):
            future.job_id = 1
        with pytest.raises(TimeoutError):
            future.result(timeout=0)
        assert tcp_io.job_test_client(env, ({"response"}, None)) == {"question"}
        assert future.result() == {"response"}

        while gc.collect():
            pass
        assert set(handler.get_job_ids()) == {1}

        with handler.start_job_io({"question"}) as (script, env, future):
            future.job_id = 2
        future.cancel()
        with pytest.raises(CancelledError):
            future.result()

        while gc.collect():
            pass
        assert set(handler.get_job_ids()) == {2}

    del future
    while gc.collect():
        pass
    assert not handler.get_job_ids()


def test_init_free_port():
    min_port = 59000
    max_port = 59003
    ports = list(range(min_port, max_port + 1))

    with tcp_io._init_free_port(min_port=min_port, max_port=max_port) as (_, port):
        assert port in ports

    with _open_sockets(min_port, max_port - 1):
        with tcp_io._init_free_port(min_port=min_port, max_port=max_port) as (_, port):
            assert port in ports

    with _reserve_sockets(min_port, max_port - 1):
        with tcp_io._init_free_port(min_port=min_port, max_port=max_port) as (_, port):
            assert port in ports

    with _open_sockets(min_port, max_port):
        with tcp_io._init_free_port(min_port=min_port, max_port=max_port) as (_, port):
            assert port not in ports

    with _reserve_sockets(min_port, max_port):
        with tcp_io._init_free_port(min_port=min_port, max_port=max_port) as (_, port):
            assert port not in ports


@contextmanager
def _open_sockets(min_port, max_port):
    host = tcp_io._get_host()
    with ExitStack() as stack:
        for port in range(min_port, max_port + 1):
            sock = stack.enter_context(socket.socket())
            sock.bind((host, port))
        yield


@contextmanager
def _reserve_sockets(min_port, max_port):
    with ExitStack() as stack:
        for port in range(min_port, max_port + 1):
            stack.enter_context(
                tcp_io._init_free_port(min_port=min_port, max_port=max_port)
            )
        yield
