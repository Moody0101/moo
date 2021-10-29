
from shutil import copy
from os import system, remove, path, environ, scandir, mkdir
from time import sleep
from sys import argv, exit
from itertools import chain

class mooInstaller:
    def __init__(self):
        self.dirs = ["./oscommands", "./gitcommands", "./oscommands/hashingCommands"]
        if len(argv) > 1:
            self.env = argv[1]
            if not path.exists(self.env):
                print("the path you gave does not exist")
                exit()
            else:
                if not path.exists(f"{self.env}/dist"):
                    mkdir(f"{self.env}/dist")
            self.scan(argv[2])
        else:
            print("Nothing was specified!")
            exit()
        print("script => ", self.Pyfile, "env =>", self.env)
        self.install()
    def scan(self, name) -> str:
        print("scanning for the script..")
        sleep(1)
        files = list(chain.from_iterable([i.path for i in scandir(x) if "py" in i.name.split('.') and i.name == name] for x in self.dirs))
        if len(files) < 1:
            print("script does not exist!!")
            exit()
        self.Pyfile = str(files[0])
    
    def checkifExExist(self, executable):
        if path.exists(executable):
            Del = str(input("the script is already installed in your machine do you want to reinstall it yes/no :=> "))
            if Del.upper().strip() == "YES":
                print('reinstalling...')
                remove(executable)
            else:
                print("quiting...")
                sleep(0.5)
                exit(0)

    def install(self):
        name = argv[2].split('.')[0]
        destination = f"{self.env}/dist"
        executable = destination + f"/{name}.exe"
        self.checkifExExist(executable)
        print(f'installing {name}...')
        system(f"pyinstaller --onefile {self.Pyfile}")
        print(f"installing {name}")
        copy("./dist/" + name + ".exe", destination)
        print("the script was successfully installed!!")


if __name__ == '__main__':
    mooInstaller()
