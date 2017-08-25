#!py -2

# ! this is meant to be used as a command like program since it's python2 only \o/

import bencode
import hashlib
import base64
import sys


def generate_magnet(torrent_file):
    torrent = open(torrent_file, 'rb').read()
    metadata = bencode.bdecode(torrent)
    hashcontents = bencode.bencode(metadata['info'])
    digest = hashlib.sha1(hashcontents).digest()
    b32hash = base64.b32encode(digest)
    magnet = 'magnet:?xt=urn:btih:' + b32hash
    print(magnet)


generate_magnet(sys.argv[1])
