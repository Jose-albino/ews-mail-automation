import pytest
from exchange_automator import __version__
from exchange_automator.cli import description


@pytest.fixture
def package_version():
    return __version__


@pytest.fixture
def package_description():
    return description
