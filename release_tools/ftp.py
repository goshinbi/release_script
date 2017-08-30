from ftplib import FTP
import os.path as path
import os


def ftp_conn(url, user, passwd):
    ftp = FTP(url)
    ftp.login(user=user, passwd=passwd)
    return ftp


def ftp_put(ftp, src, dst):
    if os.path.isdir(src):
        ftp_put_folder(ftp, src, dst)
        return

    file_name = os.path.split(src)[-1]
    dst = '/'.join([dst, file_name])

    print('----> FTP: uploading file: src, dst', src, ',', dst)
    # server_folder/file and ftp_folder leads to a path of ftp_folder/file (not needed for folders)

    with open(src, 'rb') as f:
        ftp.storbinary('STOR ' + dst, f)


def ftp_put_folder(ftp, src, dst):
    print('----> FTP: uploading folder: src, dst', src, ',', dst)
    dirs = [src]

    while dirs:
        dir = dirs.pop(0)
        dir, next_dirs, next_files = next(os.walk(dir))
        next_dirs = ['\\'.join([dir, nd]) for nd in next_dirs]
        next_files = ['\\'.join([dir, f]) for f in next_files]
        dirs += next_dirs

        # traversed is dir without the parent directories of src
        parent_count = len(src.split('\\')[0: -1])
        traversed = dir.split('\\')[parent_count:]

        dir_name = os.path.split(dir)[-1]
        dir_path = '/'.join([dst] + traversed)

        ftp_mkdir(ftp, dir_path)

        for file in next_files:
            ftp_put(ftp, file, dir_path)


def ftp_exists(ftp, dst):
    path_parts = path.split(dst)
    parent = path_parts[0: -1]
    parent = '/'.join(parent)
    return dst in ftp.nlst(parent)


def ftp_mkdir(ftp, dst):
    print('----> FTP: creating folder: dst', dst)
    if not ftp_exists(ftp, dst):
        ftp.mkd(dst)

