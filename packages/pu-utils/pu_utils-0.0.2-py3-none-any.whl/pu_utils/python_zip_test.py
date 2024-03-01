from pathlib import Path

from ward import test

from pu_utils.python_zip import pip_install

PROJECT_DIR = Path(__file__).parents[1]
FIXTURES_DIR = PROJECT_DIR.joinpath("fixtures")
TMP_DIR = PROJECT_DIR.joinpath("tmp")


@test("`pip install ...` to a target directory", tags=["network"])
def _() -> None:
    target = TMP_DIR.joinpath("python-zip-pip-install-test")
    pip_install(FIXTURES_DIR.joinpath("python_zip_requirements.txt"), target)
    assert target.joinpath("attrs").exists()


@test("`uv pip install ...` to a target directory", tags=["network"])
def _() -> None:
    target = TMP_DIR.joinpath("python-zip-uv-pip-install-test")
    pip_install(FIXTURES_DIR.joinpath("python_zip_requirements.txt"), target)
    assert target.joinpath("attrs").exists()
