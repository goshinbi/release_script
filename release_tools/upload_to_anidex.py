import subprocess
import os.path as path
from release_tools.filename_parsers import get_group


def upload_to_anidex(config, batch, private, torrent_path):
    group = get_group(torrent_path)

    anidex = config['group'][group]['anidex']
    apikey = anidex['anidex_api_key']
    group_id = anidex['group_id']
    description = anidex['description']
    anidex_script = path.join('release_tools', 'aniDex.py')

    command = [
            'py',
            '-3',
            anidex_script,
            '-a', apikey,
            '-f', torrent_path,
            '-c', '1',
            '-l', '1',
            '-g', group_id,
            '-d', description,
            '--tt'
    ]
    if batch:
        command.append('--batch')
    if private:
        command.append('--private')

    try:
        return subprocess.check_output(command).decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(e.output.decode('utf-8'))
