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

- You can either `delete`, `execute`, or `create` a config

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
### Creating a config
- Remember to put the paths inside  `"quotation marks"`
- Example usage: `script.py create -fn programmingConfig -p "path\to\Microsoft VS Code\Code.exe" "path\to\spotify.exe" -b firefox -bp "path\to\firefox.exe" -l stackoverflow.com github.com protonmail.com`
- The image below contains all the browsers supported
![image](https://user-images.githubusercontent.com/79015256/133335842-2e72bdb4-c142-4247-abeb-2b9814b83a58.png)


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
### Executing a config
- Example usage: `script.py execute programmingConfig`
```git
usage: script.py execute [-h] filename

positional arguments:
  filename    The file you want to execute

optional arguments:
  -h, --help  show this help message and exit
```
### Deleting a config
- Example usage: `script.py delete programmngConfig`
```git
usage: script.py delete [-h] filename

positional arguments:
  filename    The file you want to delete

optional arguments:
  -h, --help  show this help message and exit
```
