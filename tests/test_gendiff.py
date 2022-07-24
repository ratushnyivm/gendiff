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

path_file1_json = 'tests/fixtures/file1.json'
path_file2_json = 'tests/fixtures/file2.json'


def test_generate_diff_json():
    assert generate_diff(path_file1_json, path_file2_json) ==\
           result_gendiff


path_file1_yml = 'tests/fixtures/file1.yml'
path_file2_yml = 'tests/fixtures/file2.yml'


def test_generate_diff_yml():
    assert generate_diff(path_file1_yml, path_file2_yml) ==\
           result_gendiff
