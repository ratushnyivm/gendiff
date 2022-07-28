from collections import OrderedDict
import itertools


def stylish_render(file: dict):

    def iter_(value, depth):

        if not isinstance(value, dict):
            return str(value)

        sorted_file = OrderedDict(sorted(value.items(), key=lambda t: t[0]))

        lines = []
        spaces_count = 1
        deep_indent_size = depth + spaces_count
        condition = {
            'added': '  + ',
            'deleted': '  - ',
            'changed': '    ',
            'unchanged': '    '
        }
        replacer = '    '
        deep_indent = replacer * (deep_indent_size - 1)
        current_indent = replacer * depth

        for key, value in sorted_file.items():

            if not isinstance(value, dict):
                lines.append(
                    f"{deep_indent}"
                    f"{condition['unchanged']}"
                    f"{key}: "
                    f"{value}"
                )

            elif value.get('value'):
                lines.append(
                    f"{deep_indent}"
                    f"{condition[value.get('status', 'unchanged')]}"
                    f"{key}: "
                    f"{iter_(value.get('value'), deep_indent_size)}"
                )

            elif value.get('old_value') or value.get('new_value') \
                    or value.get('status') == 'changed':
                lines.append(
                    f"{deep_indent}"
                    f"{condition['deleted']}"
                    f"{key}: "
                    f"{iter_(value.get('old_value'), deep_indent_size)}"
                )
                lines.append(
                    f"{deep_indent}"
                    f"{condition['added']}"
                    f"{key}: "
                    f"{iter_(value.get('new_value'), deep_indent_size)}"
                )

            else:
                lines.append(
                    f"{deep_indent}"
                    f"{condition[value.get('status', 'unchanged')]}"
                    f"{key}: "
                    f"{iter_(value.get('value', value), deep_indent_size)}"
                )

        result = itertools.chain("{", lines, [current_indent + "}"])

        return '\n'.join(result).replace('True', 'true')\
            .replace('False', 'false').replace('None', 'null')

    return iter_(file, 0)
