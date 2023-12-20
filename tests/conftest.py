import pathlib
import pytest

from bookwires.paths import PROJECT_ROOT

@pytest.fixture
def samples_path() -> pathlib.Path:
    return PROJECT_ROOT / 'tests' / 'samples'