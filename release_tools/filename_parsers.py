import re
import os.path as path


def get_group(file):
    file = path.split(file)[-1]
    group_pattern = re.compile('\[(.+)\]\s')
    group = group_pattern.findall(file)[0]  # assume group is the first thing between square brackets
    return group


def get_anime_title(file):
    print('FILE:', file, path.isfile(file), path.getsize(file))
    if path.isfile(file):
        file = path.split(file)[-1]
        title_pattern = re.compile('\] (.+) - ')
    else:
        file = path.split(file)[-1]
        print('FOLDER IS NOW:', file)
        title_pattern = re.compile('\] (.+) \(')

    title = title_pattern.findall(file)[0]
    return title


print(get_anime_title('C:\\Users\\chris\\Downloads\\[testdesuyo] Anime Tenchou season 6 - 01 (BD 1920x1080 10bit FLAC).mkv'))