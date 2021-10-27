from sys import argv
from variables import CatDoc, v
from fileinput import input
class Cat:
    def __init__(self, file: str = None, files: list[str] = None) -> None:
        self.file = file
        self.files = files
    
    def cat(self) -> None:
        for line in input(self.file):
            print(line)
    def execute(self):
        if len(argv) == 2:
            if '-v' in argv:
                print(v)
            else:
                self.file = argv[1]
                self.cat()
        elif len(argv) == 1:
            print(CatDoc)
    def __repr__(self) -> str:
        return '<Command: cat>'


cat101: Cat = Cat()
if __name__ == '__main__':
    cat101.execute()