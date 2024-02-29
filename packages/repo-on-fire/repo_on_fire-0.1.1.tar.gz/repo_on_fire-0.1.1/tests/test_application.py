"""Test the application class."""

import pytest
from repo_on_fire.application import Application
from repo_on_fire.configuration import Configuration


def test_constructor():
    """Test if we can construct an application object."""
    Application(configuration=Configuration())


def test_help():
    """Test if we can show the help on the command line."""
    app = Application(configuration=Configuration())
    app.run_command_line(args=["--help"])


def test_help_repo_command():
    """Test if we can show the help for a repo command."""
    app = Application(configuration=Configuration())
    with pytest.raises(SystemExit):
        app.run_command_line(args=["sync", "--help"])
