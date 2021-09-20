from sys import argv
from time import sleep
from os import system
from variables import compilecDoc, v

class compile:

    def __init__(self, fileName: str=None):
        self.fileName = fileName
        self.validExt = ["cpp", "c"]
        self.compilers = ["gcc -o", "g++ -o"]
    def comp(self):
        co = True
        if self.ext == "cpp":
            while co:
                system(
                        f"{self.compilers[1]} {self.fileName.split('.')[0]} {self.fileName}"
                        )
                print(f"compiling to {self.fileNam.split('.')[0]}...")
                sleep(3)
        else:
            while co:
                system(
                            f"{self.compilers[0]} {self.fileName.split('.')[0]} {self.fileName}"
                     )
                print(f"compiling to {self.fileName.split('.')[0]}")
                sleep(3)
    def checkExt(self):
        self.ext = self.fileName.split('.')[1]
        if self.ext not in self.validExt:
            print("invalid extention: compiling cpp, c files only")
            exit()
        else:
            self.comp()

    def execute(self):
        if len(argv) > 2 or len(argv) == 1:
            print("Invalid syntax: compile <fileName>")
        elif len(argv) == 2:
            if argv[1] == "--help" or argv[1] == "-h":
                print(compilecDoc)
            elif argv[1] == "--version" or argv[1] == "-v":
                print(v)
            else:
                self.fileName = argv[1]
                self.checkExt()


def main():

    compiler = compile()
    compiler.execute()


if __name__ == '__main__':
    main()

