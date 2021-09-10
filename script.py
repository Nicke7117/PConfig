import os
import argparse
import subprocess
import webbrowser
from pathlib import Path

class Config:
    def __init__(self, name, paths, links, browser):
        self.name = name
        self.paths = paths
        self.links = links
        self.browser = browser

    def create_config(self):
        try:
            filename = self.name + ".txt"
            file_exists(filename)
            file = open(os.path.join(folder_path, filename), "w")
            if self.paths:
                print(self.paths)
                file.write("Paths: \n")
                for i in range(len(self.paths)):
                    file.write(self.paths[i] + "\n")
            if self.links:
                file.write("Links: \n")
                for i in range(len(self.links)):
                    file.write(self.links[i] + "\n")
            if self.browser:
                file.write("Browser: \n")
                file.write(self.browser)
            file.close()
        except Exception as e:
            print(e)

def execute(name):
    try:
        filename = name + ".txt"
        string_type = None
        with open(os.path.join(folder_path, filename), "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                line = lines[i].strip()
                list = ["Paths:", "Links:", "Browser:", "Browser path:"]
                if not line:
                    break
                if line in list:
                    string_type = line
                    continue
                if string_type == "Paths:":
                    try:
                        subprocess.call(line)
                    except subprocess.CalledProcessError:
                        print("It is not possible to execute " + line)
                elif string_type == "Browser:":
                    global browser
                    browser = line
                elif string_type == "Browser path:":
                    global browser_path
                    browser_path = line
                elif string_type == "Links:":
                    try:
                        webbrowser.register(browser, None, webbrowser.BackgroundBrowser(browser_path))
                        webbrowser.get(browser).open_new_tab(line)
                        print("Succesfull")
                    except Exception as e:
                        print(e)
    except FileExistsError as error:
        print(error)


def delete():
    pass


parser = argparse.ArgumentParser(description="Create, execute or delete a config")

subparser = parser.add_subparsers(dest="command")

parser_execute = subparser.add_parser("execute", help="Execute config")
parser_execute.add_argument("filename" , type=str, help="The file you want to execute")


parser_create = subparser.add_parser("create")
parser_create.add_argument("-p", "--paths", type=str, nargs="*")
parser_create.add_argument("-l", "--links", type=str, nargs="*")
parser_create.add_argument("-b", "--browser", type=str)
parser_create.add_argument("-bp", "--browserpath", type=str)
required_args = parser_create.add_argument_group("required arguments")
required_args.add_argument("-fn", "--filename", type=str, required=True)

parser_create = subparser.add_parser("delete")

args = parser.parse_args()

folder_path = "C:\\Users\\nikol\\Desktop\\StartupConfig"

if __name__ == "__main__":
    print(folder_path)
    if args.command == "create":
        print(args.paths)
        config = Config(args.filename, args.paths, args.links, args.browser)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        config.create_config()
    elif args.command == "execute":
        execute(args.filename)
        print("execute")
    elif args.command == "delete":
        print("delete")
