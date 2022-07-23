from gendiff.gendiff import stringify
from gendiff import generate_diff  # noqa


def test_stringify():
    assert stringify(5) == '5'


result_gendiff = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

path_file1 = 'tests/fixtures/file1.json'
path_file2 = 'tests/fixtures/file2.json'


def test_generate_diff():
    assert generate_diff(path_file1, path_file2) == result_gendiff
