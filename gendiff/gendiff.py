import json
import os
import yaml
from gendiff.output_views.stylish import stylish_output
from gendiff.output_views.json import json_output


def extract_data(path: str) -> dict:
    absolute_path = os.path.abspath(path)

    with open(absolute_path) as import_file:
        if absolute_path.endswith('.yml') or absolute_path.endswith('.yaml'):
            result = yaml.safe_load(import_file)
        elif absolute_path.endswith('.json'):
            result = json.load(import_file)

    return result


def make_diff(file1: dict, file2: dict) -> dict:
    keys = file1.keys() | file2.keys()
    result = {}

    for key in keys:
        # КЛЮЧ ОТСУТСТВУЕТ В ПЕРВОМ ФАЙЛЕ И ПРИСУТСТВУЕТ ВО ВТОРОМ
        if key not in file1:
            result[key] = {
                'status': 'added',
                'value': file2.get(key)
            }
        # КЛЮЧ ПРИСУТСТВУЕТ В ПЕРВОМ ФАЙЛЕ И ОТСУТСТВУЕТТ ВО ВТОРОМ
        elif key not in file2:

            result[key] = {
                'status': 'deleted',
                'value': file1.get(key)
            }

        # ПАРЫ КЛЮЧ/ЗНАЧЕНИЯ ОДИНАКОВЫ В ОБОИХ ФАЙЛАХ
        elif file1[key] == file2[key]:

            if isinstance(file1[key], dict) and \
                    isinstance(file2[key], dict):

                result[key] = {
                    'status': 'unchanged',
                    'value': make_diff(file1[key], file2[key])
                }

            else:
                result[key] = {
                    'status': 'unchanged',
                    'value': file1.get(key)
                }
        # КЛЮЧ ПРИСУТСТВУЕТ В ОБОИХ ФАЙЛАХ, ЗНАЧЕНИЯ ОТЛИЧАЮТСЯ
        else:
            # ЗНАЧЕНИЯ В ОБОИХ ФАЙЛАХ ЯВЛЯЮТСЯ СЛОВАРЯМИ
            if isinstance(file1[key], dict) and \
                    isinstance(file2[key], dict):
                result[key] = {
                    'status': 'changed',
                    'value': make_diff(file1[key], file2[key])
                }
            else:
                result[key] = {
                    'status': 'changed',
                    'old_value': file1[key],
                    'new_value': file2[key]
                }

    return result


def generate_diff(
        file_path1: str,
        file_path2: str,
        format_name: str = 'stylish'
):

    file_data1, file_data2 = extract_data(file_path1), extract_data(file_path2)
    data_diff = make_diff(file_data1, file_data2)

    if format_name == 'stylish':
        return stylish_output(data_diff)
    elif format_name == 'plain':
        return 'plain'
    elif format_name == 'json':
        return json_output(data_diff)

    return None
