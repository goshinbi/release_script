## This includes copies of anidex.py and api_uploader_v2.py you can find links to both of the github pages below
https://github.com/Golumpa/AniDexPy

https://github.com/nyaadevs/nyaa/blob/master/utils/api_uploader_v2.py


# DDY Distro Process
#### If you are releasing a show that hasn't been released with the tool, complete the following. Otherwise skip to step 3.

## 1. Copy the below json template section.

        "[INSERT SHOW NAME HERE WITHOUT BLOCK PARENTHESIS]": {
			"groups": {
                "Group_ichi": {
                    "wordpress tagline": "",
                    "mega": {
                        "account": "*********@gmail.com",
                        "pass": "*********"
                    }
                },
                "Group_ni": {
                    "wordpress tagline": "",
                    "mega": {
                        "account": "*********@gmail.com",
                        "pass": "*********"
                    }
                }
            }
        }

## 2. Edit the settings.json file with notepad++. ( Or vim like a real nerd ;3 )

### 2a. Add a comma after the last show added's final }.
### 2b. Paste the template in after the last show added.
### 2c. Fill in the details for show name, mega account and password. Group names can be modified if needed. May include more than 2 as well.
### 2d. Save the file.

## 3.  Open a command prompt. enter the following commands, each followed by clicking "enter".

```
    cd E:\distro
    release_script "[full path to file\folder]"
```

### 4. for example:
```
	release_script "E:\DDY\BDs\Soushin Shoujo Matoi\[BlurayDesuYo] Soushin Shoujo Matoi - Vol. 2 (BD 1920x1080 10bit FLAC)"
```
## 5. When it is done, right click in the cmd prompt and choose "Mark" then select the links provided in the summary at the end.
## 6. Click "enter" to copy the links.
## 7. Paste the links somewhere so you can add them to your blog post.

# Caveats:

	If uploading a folder, do not include a \ at the end of the file path. It will break things.
	The Mega upload portion creates a folder at the root of the Mega account by the show title (pulled from the files) if one does not already exist. You may have to move existing files from before this tool was created to the new folder. May be fixed in a later version of the distro app.
	If uploading a folder, the Mega upload portion just uploads to the root of the Mega account. You may have to move the files to the appropriate directory. May be fixed in a later version of the distro app.


The script accepts parameters for individual actions.. It also includes "batch" and "private" options. By default the script runs everything but these two options.

Note that Nyaa.si's and Anidex's private mode work differently. For Anidex, a private torrent can only be seen by accounts listed as "Staff" on the site.

## =====================================================

## The help file is below.

```
usage: DDY_release_app.py [-h] [--mega_account MEGA_ACCOUNT]
                          [--megapass MEGAPASS] [--mktorrent] [--magnet]
                          [--ftp] [--mega] [--batch] [--anidex] [--nyaasi]
                          [--private]
                          input

Capitalization of the group name in the settings file must match the group
name in the file/folder! mktorrent, magnet, ftp, mega, anidex, and nyaasi can
be run on their own. otherwise all of those steps will be performed. you can
run any combination of them. (many of these of course depend on having created
the torrent already, and possibly others.)

positional arguments:
  input                 Folder or file from which to create the torrent

optional arguments:
  -h, --help            show this help message and exit
  --mega_account MEGA_ACCOUNT
                        Mega account to switch over to (uses default pass,
                        otherwise use --megapass)
  --megapass MEGAPASS   speficy to use this password for a new mega account
                        for the show
  --mktorrent           run this step individually
  --magnet              run this step individually
  --ftp                 run this step individually
  --mega                run this step individually
  --batch               specify that this a batch
  --anidex              run this step individually
  --nyaasi              run this step individually
  --private             specify it as private/hidden on both

  ```
