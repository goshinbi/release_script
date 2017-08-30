def double_quote(string):
    return '"' + string + '"'


def remove_double_quote(string):
    if string[0] == '"' and string[-1] == '"':
        return string[1:-1]
    else:
        return string


def remove_file_extension(file):
    return ''.join(file.split('.')[0:-1])
