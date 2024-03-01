import pytest


@pytest.mark.parametrize("pre_script", [None, "echo 'run pre script'"])
@pytest.mark.parametrize("post_script", [None, "echo 'run post script'"])
def test_python_script(pre_script, post_script, slurm_python_client):
    future = slurm_python_client.spawn(
        sum, args=([1, 1],), pre_script=pre_script, post_script=post_script
    )
    try:
        assert future.result() == 2
        assert slurm_python_client.get_status(future.job_id) == "COMPLETED"
    finally:
        slurm_python_client.print_stdout_stderr(future.job_id)
        slurm_python_client.clean_job_artifacts(future.job_id)


def test_python_script_with_failure(slurm_python_client):
    future = slurm_python_client.spawn(job_with_failure)
    try:
        with pytest.raises(RuntimeError, match="top failure message"):
            future.result()
        assert slurm_python_client.get_status(future.job_id) == "COMPLETED"
    finally:
        slurm_python_client.print_stdout_stderr(future.job_id)
        slurm_python_client.clean_job_artifacts(future.job_id)


def test_python_script_with_chained_failure(slurm_python_client):
    future = slurm_python_client.spawn(job_with_chained_failure)
    try:
        with pytest.raises(RuntimeError, match="top failure message") as exc_info:
            future.result()
        assert slurm_python_client.get_status(future.job_id) == "COMPLETED"
    finally:
        slurm_python_client.print_stdout_stderr(future.job_id)
        slurm_python_client.clean_job_artifacts(future.job_id)
    assert isinstance(exc_info.value.__cause__, ValueError)
    assert str(exc_info.value.__cause__) == "cause failure message"


def test_python_script_with_error_handling_failure(slurm_python_client):
    future = slurm_python_client.spawn(job_with_error_handling_failure)
    try:
        with pytest.raises(RuntimeError, match="top failure message") as exc_info:
            future.result()
        assert slurm_python_client.get_status(future.job_id) == "COMPLETED"
    finally:
        slurm_python_client.print_stdout_stderr(future.job_id)
        slurm_python_client.clean_job_artifacts(future.job_id)
    assert isinstance(exc_info.value.__context__, ValueError)
    assert str(exc_info.value.__context__) == "context failure message"


def job_with_failure():
    raise RuntimeError("top failure message")


def job_with_chained_failure():
    try:
        raise ValueError("cause failure message")
    except ValueError as e:
        raise RuntimeError("top failure message") from e


def job_with_error_handling_failure():
    try:
        raise ValueError("context failure message")
    except ValueError:
        raise RuntimeError("top failure message")
