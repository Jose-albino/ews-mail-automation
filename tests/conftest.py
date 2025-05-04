import pytest
from exchange_automator import __version__

@pytest.fixture
def package_version():
    return __version__