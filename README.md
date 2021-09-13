# PConfig
PConfig is a script that helps you to make windows configurations. You can make the config open urls in your browser and start windows apps. You could use this script to create a config for example for your mathematics class, the script could start your calculator and open your notes and other stuff from your browser with a single command.

## Installation
- Clone the repository

```git
git clone https://github.com/Nicke7117/PConfig.git
```
- Change your current directory to the PConfig repository

## Setting up

- Open ```Constants.py ```
- Add the folder path you want to store the .txt config files to ```FOLDER_PATH```, for example ```FOLDER_PATH = "C:\Users\user123\desktop"```

## Usage

- First you have to either select `delete`, `execute`, or `create`

```git
usage: script.py [-h] {delete,execute,create} ...

Create, execute or delete a config

positional arguments:
  {delete,execute,create}
    delete              Delete config
    execute             Execute config

optional arguments:
  -h, --help            show this help message and exit
```
- Here are the arguments for creating a config

```git
usage: script.py create [-h] [-p [PATHS ...]] [-l [LINKS ...]] [-b BROWSER] [-bp BROWSERPATH] -fn FILENAME

optional arguments:
  -h, --help            show this help message and exit
  -p [PATHS ...], --paths [PATHS ...]
  -l [LINKS ...], --links [LINKS ...]
  -b BROWSER, --browser BROWSER
  -bp BROWSERPATH, --browserpath BROWSERPATH

required arguments:
  -fn FILENAME, --filename FILENAME
```
- The arguments if you want to execute a config
```git
usage: script.py execute [-h] filename

positional arguments:
  filename    The file you want to execute

optional arguments:
  -h, --help  show this help message and exit
```
- The arguments if you want to delete a config
```git
usage: script.py delete [-h] filename

positional arguments:
  filename    The file you want to delete

optional arguments:
  -h, --help  show this help message and exit
```
