import subprocess
import re
import os.path as path


def file_size(file):
    return path.getsize(file)


def space_used():
    command = ['MEGAclient', 'du']
    output = subprocess.check_output(command).decode('utf-8')
    print('OUTPUT:', output)
    return int(re.compile('\d+').findall(output)[0])


def sufficient_space(file):
    used = space_used()
    size = file_size(file)
    return size + used < 53687091000


def mega_put(src, title=None):
    if title == None:
        dst = '/'
    else:
        dst = '/' + title + '/'
    command = ['MEGAclient', 'put', src, '-c', dst]
    print('COMMAND:', command)
    subprocess.run(command)
