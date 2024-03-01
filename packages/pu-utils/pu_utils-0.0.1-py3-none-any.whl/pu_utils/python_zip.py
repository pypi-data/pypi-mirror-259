import subprocess
from pathlib import Path
from shutil import rmtree


def pip_install(requirements_path: str | Path, target_path: str | Path) -> None:
    requirements_path = Path(requirements_path)
    target_path = Path(target_path)

    rmtree(target_path, ignore_errors=True)
    command = [
        "pip",
        "install",
        "-r",
        requirements_path,
        "--target",
        target_path,
        "--only-binary",
        ":all:",
        "--platform",
        "manylinux2014_x86_64",
        "--implementation",
        "cp",
    ]
    process = subprocess.run(command, capture_output=True, check=False)
    if process.returncode != 0:
        print(process.stderr.decode())  # noqa: T201
        process.check_returncode()


def uv_pip_install(requirements_path: str | Path, target_path: str | Path) -> None:
    """Same as pip_compile but is much faster and requires installing `uv` first"""

    requirements_path = Path(requirements_path)
    target_path = Path(target_path)

    rmtree(target_path, ignore_errors=True)
    command = [
        "uv",
        "pip",
        "install",
        "-r",
        requirements_path,
        "--target",
        target_path,
        "--only-binary",
        ":all:",
        "--platform",
        "manylinux2014_x86_64",
        "--implementation",
        "cp",
    ]
    process = subprocess.run(command, capture_output=True, check=False)
    if process.returncode != 0:
        print(process.stderr.decode())  # noqa: T201
        process.check_returncode()
