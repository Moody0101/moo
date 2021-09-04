from os import remove
from variables import v, DelDoc
from sys import argv

class delete:
    def __init__(self, file: str = None, files: list[str] = None) -> None:
        self.file = file
        self.files = files
    def delete(self):
        if self.file:
            remove(self.file)
        elif self.files:
            for _ in self.files:
                remove(_)
    def execute(self) -> None:
        if len(argv) == 1:
            print(DelDoc)
        elif len(argv) == 2:
            if '-v' in argv:
                print(v)
            elif '-h' in argv:
                print(f"Help : \n {DelDoc}")
            else:
                self.file = argv[1]
        elif len(argv) > 3:
            self.files = argv[1::]
        self.delete()
    def __repr__(self) -> str:
        return '<Command: delete>'




del101 = delete() 
if __name__ == '__main__':
    del101.execute()

