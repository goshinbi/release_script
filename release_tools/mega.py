import subprocess
import re
import os.path as path


def file_size(file):
    return path.getsize(file)


def space_left():
    command = ['MEGAclient', 'du']
    return int(re.compile('\d+').findall(subprocess.check_output(command).decode('utf-8'))[0])


def sufficient_space(file):
    space = space_left()
    size = file_size(file)
    return space > size


def mega_put(src, title=None):
    if title == None:
        dst = '/'
    else:
        dst = '/' + title + '/'
    command = ['MEGAclient', 'put', src, '-c', dst]
    print('COMMAND:', command)
    subprocess.run(command)
