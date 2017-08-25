import subprocess


print('make sure mega tools and mktorrent are in your path variable')
input('(press enter)\n')

print('install both python 2 and 3 if you haven\'t')
input('(press enter)\n')

print('add DDY_release_script folder to your path')
input('(press enter)\n')

print('update the settings.json file')
input('(press enter)\n')

print('add the full path of DDY_release_app_installer.py to the release_script.bat file')
input('(press enter)\n')

print('attempting to install all requirements, hopefully I didn\'t forget any x3')
print(subprocess.check_output(['py', '-3', '-m', 'pip', 'install', 'requests']).decode('utf-8'))
print(subprocess.check_output(['py', '-2', '-m', 'pip', 'install', 'bencode']).decode('utf-8'))
input('press enter\n')

print('all set! just run the program with release_script args')
input('press enter\n')
