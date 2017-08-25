import subprocess
import os.path as path
from release_tools.filename_parsers import get_group


def upload_to_nyaasi(config, batch, hidden, torrent_path):
    group = get_group(torrent_path)
    # description?
    nyaasi = config['group'][group]['nyaasi']
    information = nyaasi['information']

    user = nyaasi['username']
    passwd = nyaasi['pass']
    description = nyaasi['description']
    nyaasi_script = path.join('release_tools', 'api_uploader_v2.py')

    command = [
            'py',
            '-3',
            nyaasi_script,
            '-u', user,
            '-p', passwd,
            '-c', '1_2',
            '-d', description,
            '-i', information
    ]
    if batch:
        command.append('--complete')    # how nyaasi handles batches
    if hidden:
        command.append('--hidden')

    command.append(torrent_path)

    print(torrent_path)
    try:
        return subprocess.check_output(command).decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(e.output.decode('utf-8'))
