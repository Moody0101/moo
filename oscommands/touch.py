from os import mkdir, path
from funcs import createFile, creatHTML, creatPYTHON, creatCPP
from sys import argv
from variables import TouchDoc, v
class touch:

    def __init__(self, files: list[str] = None, file:str = None) -> None:
        self.file = file
        self.files = files
    def __repr__(self) -> str:
        return '<Command: touch>'
    def writeFile(self):
        if self.file.endswith('.html'):
            creatHTML(self.file) 
        elif self.file.endswith('.py'):
            creatPYTHON(self.file)
        elif self.file.endswith('.cpp'):
            creatCPP(self.file)
        else:
            createFile(" ", self.file)
            
    def touch0(self) -> int:
        """
        passing attribs to the writefile function
        """
        if self.file:
            self.writeFile() 
        elif self.files:
            for _ in self.files:
                self.file = str(_)
                self.writeFile()
        return 0
    def execute(self):
        """
        this method makes decisions based on argvs.
        """
        if len(argv) == 1:
            print(TouchDoc)
            return
        if '-v' in argv:
            print(v)
            return
        elif len(argv) == 2 and '-v' not in argv:
            self.file = argv[1]

        elif len(argv) > 2:
            self.files = argv[1:]
        else:
            print(TouchDoc)
            return
        self.touch0()
   


touch101 = touch() 
if __name__ == '__main__':
    touch101.execute()

