import subprocess
import os
from release_tools import path_formatter as pf


def make_torrent(announces, comment, target):
    announces = [announces[a] for a in announces]
    announce_args = []
    for announce in announces:
        announce_args.append('-a')
        announce_args.append(announce)

    prevdir = os.getcwd()
    os.chdir(os.path.split(target)[0])
    target = os.path.split(target)[1]

    output_file = target + '.torrent'
    output_file = pf.remove_double_quote(output_file)
    target = pf.remove_double_quote(target)

    command = ['mktorrent'] + announce_args + ['-c', comment, '-o', output_file, target]
    subprocess.run(command, stdout=subprocess.PIPE)

    os.chdir(prevdir)
