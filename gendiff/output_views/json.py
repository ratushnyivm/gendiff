from collections import OrderedDict
import json


def json_output(file: dict):
    sorted_file = OrderedDict(sorted(file.items(), key=lambda t: t[0]))
    return json.dumps(sorted_file)
