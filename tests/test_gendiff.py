from gendiff.gendiff import stringify
from gendiff import generate_diff  # noqa


def test_stringify():
    assert stringify(5) == '5'


def test_generate_diff():
    pass

