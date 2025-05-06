import nox


@nox.session(python=["3.8", "3.9", "3.10"])
def tests(session):
    session.install("-e", ".[dev]")
    session.run("pytest")


@nox.session
def lint(session):
    session.install("ruff")
    session.run("ruff", "my_package", "tests")


@nox.session
def type_check(session):
    session.install("mypy")
    session.run("mypy", "my_package")


@nox.session
def format(session):
    session.install("black")
    session.run("black", "my_package", "tests")
