import os.path as path
import sys
from release_tools.ftp import *
from release_tools.filename_parsers import get_group


def put_up_release(url, user, passwd, mkv_src, mkv_dst, trt_src, trt_dst):
    ftp = ftp_conn(url, user, passwd)

    if not ftp_exists(ftp, mkv_dst):
        ftp_mkdir(ftp, mkv_dst)
    if not ftp_exists(ftp, trt_dst):
        ftp_mkdir(ftp, trt_dst)

    print(mkv_src, ', ', mkv_dst)
    print(trt_src, ', ', trt_dst)

    print('uploading mkv to ftp...', mkv_src, ', ', mkv_dst)
    ftp_put(ftp, mkv_src, mkv_dst)
    print('uploading torrent to ftp...')
    ftp_put(ftp, trt_src, trt_dst)
    ftp.close()
    print('completed ftp upload successfully')


def upload_to_ftp(config, mkv, torrent):
    if not path.exists(torrent):
        inp = input('No torrent found! Continue? y/n')
        if inp != 'Y' and inp != 'y':
            sys.exit()

    group = get_group(mkv)

    if group not in config['group']:
        print('Group not found! using default')
        group = 'default'

    ftp_config = config['group'][group]['ftp']

    url = ftp_config['url']
    user = ftp_config['username']
    passwd = ftp_config['pass']
    torrent_folder = ftp_config['torrent_folder']
    mkv_folder = ftp_config['mkv_folder']

    put_up_release(url, user, passwd, mkv, mkv_folder, torrent, torrent_folder)
