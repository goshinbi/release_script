import os
from release_tools.mega import *
from release_tools.filename_parsers import get_anime_title, get_group


def upload_to_mega(config, mkv_path, batch):
    group = get_group(mkv_path)
    title = get_anime_title(mkv_path, batch)
    show = config['shows'][title]['groups'][group]
    mega = show['mega']

    print('starting MEGAcmd...')
    os.system(' '.join(['start', '""', 'MEGAcmd.exe']))

    # login
    print('attempting to log into mega...')

    try:
        output = subprocess.check_output(['MEGAclient', 'login', mega['account'], mega['pass']]).decode('utf-8')
        print('successfully logged in')
    except subprocess.CalledProcessError:
        pass    # I don't know why it raises this \o/

    if sufficient_space(mkv_path):
        if path.isfile(mkv_path):
            mega_put(mkv_path, title)
        else:
            mega_put(mkv_path)

    else:
        print('!!! not enough space')

    # log out
    print('attempting to log out of mega...')
    print(subprocess.check_output(['MEGAclient', 'logout']).decode('utf-8'))

    # try to close
    print('attempting to close the program')
    print(subprocess.check_output(['taskkill', '/im', 'MEGAcmd.exe']))
