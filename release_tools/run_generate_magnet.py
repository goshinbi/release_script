import subprocess
import os.path as path


def generate_magnet(torrent_file):
    # run generate_magnet.py as a python2 command line app
    # the packages it relies on don't seem to work under python 3
    # this lets me avoid mixing versions of python
    generate_magnet_path = path.join('release_tools', 'generate_magnet.py')
    return subprocess.check_output(['py', '-2', generate_magnet_path, torrent_file]).decode('utf-8')
