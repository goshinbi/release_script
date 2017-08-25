#! python3

import release_tools
import argparse
import json
from math import ceil
import os
import sys
from release_tools.filename_parsers import *


script_dir = os.path.dirname(__file__)
script_dir = os.path.abspath(script_dir)
sys.path.append(script_dir)
print('VERSION', sys.version)
config_path = os.path.join(script_dir, 'settings.json')
print('CONFIG_PATH:', config_path)


def load_config():

    with open(config_path, 'r') as profile_file:
        profile = json.load(profile_file)
    return profile


def write_config(config):
    with open(config_path, 'w') as profile_file:
        json.dump(config, profile_file, indent=4)


def update_mega(args, config):
    print('updating mega')

    mkv_path = args.input
    title = get_anime_title(mkv_path)
    group = get_group(mkv_path)

    config['shows'][title]['groups'][group]['mega']['account'] = args.mega_account
    if args.megapass:
        config['shows'][title]['groups'][group]['mega']['pass'] = args.megapss
    else:
        config['shows'][title]['groups'][group]['mega']['pass'] = config['default_mega_pass']

    write_config(config)


def fancy(string):
    line_len = 30
    line = '=' * line_len
    middle_len = len(string)
    side = '=' * (int(ceil(line_len / 2)) - 1 - int(ceil(middle_len/2)))
    middle = side + ' ' + string + ' ' + side
    if len(middle) == 29:
        middle += '='
    print(line)
    print(middle)
    print(line)


def parse_args():
    parser = argparse.ArgumentParser(description='''
        Capitalization of the group name in the settings file must match the group name in the file/folder!
    
        mktorrent, magnet, ftp, mega, anidex, and nyaasi can be run on their own.
        otherwise all of those steps will be performed.
        you can run any combination of them.
        (many of these of course depend on having created the torrent already, and possibly others.)
    \n''')
    parser.add_argument("input", help="Folder or file from which to create the torrent", type=str)
    parser.add_argument("--mega_account", default=False, action='store',
                        help="Mega account to switch over to (uses default pass, otherwise use --megapass)")
    parser.add_argument("--megapass", default=False, action='store',
                        help="speficy to use this password for a new mega account for the show")
    # options for single steps'
    parser.add_argument('--mktorrent', default=False, action='store_true', help="run this step individually")
    parser.add_argument('--magnet', default=False, action='store_true', help="run this step individually")
    parser.add_argument('--ftp', default=False, action='store_true', help="run this step individually")
    parser.add_argument('--mega', default=False, action='store_true', help="run this step individually")
    parser.add_argument("--batch", default=False, action='store_true', help="specify that this a batch")
    parser.add_argument('--anidex', default=False, action='store_true', help="run this step individually")
    parser.add_argument('--nyaasi', default=False, action='store_true', help="run this step individually")
    parser.add_argument('--private', default=False, action='store_true', help="specify it as private/hidden on both")

    return parser.parse_args()


def main():
    args = parse_args()
    args.input = os.path.abspath(args.input)
    os.chdir(script_dir)
    print('CWD:', os.getcwd())
    config = load_config()
    mkv_path = args.input

    if mkv_path[-1] == chr(34):
        mkv_path = mkv_path[0:-1]
        print('changed mkv path')

    torrent_path = path.abspath(mkv_path + '.torrent')

    group = release_tools.get_group(mkv_path)
    magnet = "magnet not created"   # in case it doesn't get ran
    anidex_link = 'Not ran or received error'
    nyaasi_link = 'Not ran or received error'
    run_individual = args.mktorrent or args.magnet or args.ftp or args.mega or args.anidex or args.nyaasi

    if args.mega_account:
        fancy('MEGA_ACCOUNT')
        update_mega(args, config)

    if not run_individual or args.mktorrent:
        fancy('MKTORRENT')
        release_tools.make_torrent(config['announces'], config['group'][group]['comment'], args.input)

    if not run_individual or args.magnet:
        fancy('MAGNET')
        magnet = release_tools.generate_magnet(torrent_path)
        print(magnet)

    if not run_individual or args.ftp:
        fancy('FTP UPLOAD')
        release_tools.upload_to_ftp(config, mkv_path, torrent_path)

    if not run_individual or args.mega:
        fancy('MEGA UPLOAD')
        release_tools.upload_to_mega(config, mkv_path)

    if not run_individual or args.anidex:
        anidex_output = release_tools.upload_to_anidex(config, args.batch, args.private, torrent_path)
        print(anidex_output)
        if anidex_output.startswith('https://anidex.info/torrent/'):
            anidex_link = anidex_output

    if not run_individual or args.nyaasi:
        nyaasi_output = release_tools.upload_to_nyaasi(config, args.batch, args.private, torrent_path)
        print(nyaasi_output)
        if nyaasi_output is not None and nyaasi_output.startswith('[Uploaded] https://nyaa.si/view/'):
            pat = re.compile('https://nyaa.si/view/\d+')
            nyaasi_link = pat.findall(nyaasi_output)[0]

    print('\n\n\n\n\n')
    fancy('MAGNET & LINKS')
    print('magnet:', magnet)
    print('anidex:', anidex_link.replace('\n', ''))
    print('nyaasi:', nyaasi_link.replace('\n', ''))

main()
