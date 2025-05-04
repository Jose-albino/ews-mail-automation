from exchange_automator import __version__

def test_version_matches_expected(package_version):
    assert __version__ == package_version
