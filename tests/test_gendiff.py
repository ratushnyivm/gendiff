from gendiff.gendiff import extract_data
from gendiff import generate_diff  # noqa


result_gendiff = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

path_file1_json = 'tests/fixtures/file1.json'
path_file2_json = 'tests/fixtures/file2.json'


def test_generate_diff_json():
    assert generate_diff(path_file1_json, path_file2_json) ==\
           result_gendiff


path_file1_yml = 'tests/fixtures/file1.yaml'
path_file2_yml = 'tests/fixtures/file2.yaml'


def test_generate_diff_yml():
    assert generate_diff(path_file1_yml, path_file2_yml) ==\
           result_gendiff


file_data1 = {
    'common': {
        'setting1': 'Value 1',
        'setting2': 200,
        'setting3': True,
        'setting6': {
            'key': 'value',
            'doge': {
                'wow': ''
            }
        }
    },
    'group1': {
        'baz': 'bas',
        'foo': 'bar',
        'nest': {
            'key': 'value'
        }
    },
    'group2': {
        'abc': 12345,
        'deep': {
            'id': 45
        }
    }
}


def test_extract_data():
    assert extract_data(path_file1_json) == file_data1
    assert extract_data(path_file1_yml) == file_data1
    assert extract_data(path_file1_json) == extract_data(path_file1_yml)
    assert extract_data(path_file2_json) == extract_data(path_file2_yml)
