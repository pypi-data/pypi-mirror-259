import pytest
import pytest_twisted
import unittest.mock
from click.testing import CliRunner


from fowl.cli import invite, accept


def test_invite():
    with unittest.mock.patch("fowl.cli.react") as react:
        print(react)
        r = CliRunner()
        print('hi')
        result = r.invoke(accept, "1-foo-bar")
        print("ding")
        print(result)
        print(result.exception)
