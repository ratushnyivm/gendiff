from gendiff.gendiff import extract_data
from gendiff import generate_diff  # noqa


STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'

PATH_FILE1_JSON = 'tests/fixtures/file1.json'
PATH_FILE2_JSON = 'tests/fixtures/file2.json'
PATH_FILE1_YML = 'tests/fixtures/file1.yml'
PATH_FILE2_YML = 'tests/fixtures/file2.yml'

PATH_RESULT_STYLISH = 'tests/fixtures/result_stylish'
PATH_RESULT_PLAIN = 'tests/fixtures/result_plain'

extract_result = {
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
    assert type(extract_data(PATH_FILE1_JSON)) == dict
    assert type(extract_data(PATH_FILE1_YML)) == dict
    assert extract_data(PATH_FILE1_JSON) == extract_result
    assert extract_data(PATH_FILE1_YML) == extract_result


def test_generate_diff():

    with open(PATH_RESULT_STYLISH) as f:
        result_stylish = f.read()
    with open(PATH_RESULT_PLAIN) as f:
        result_plain = f.read()

    assert result_stylish == \
        generate_diff(PATH_FILE1_JSON, PATH_FILE2_JSON)
    assert result_stylish == \
        generate_diff(PATH_FILE1_YML, PATH_FILE2_YML)

    assert result_stylish == \
        generate_diff(PATH_FILE1_JSON, PATH_FILE2_JSON, STYLISH)
    assert result_stylish == \
        generate_diff(PATH_FILE1_YML, PATH_FILE2_YML, STYLISH)

    assert result_plain == \
        generate_diff(PATH_FILE1_JSON, PATH_FILE2_JSON, PLAIN)
    assert result_plain == \
        generate_diff(PATH_FILE1_YML, PATH_FILE2_YML, PLAIN)
