from os import mkdir, path
from funcs import createFile, creatHTML, creatPYTHON
from sys import argv
from variables import TouchDoc, v
class touch:

    def __init__(self, files: list[str] = None, file:str = None) -> None:
        self.file = file
        self.files = files
    def writeFile(self): # this function make the file and if it is a path for a dir, it checks if there is and identical dir, if there is not it makes it.
        if '\\' in self.file:
            dir = self.file.split('\\')[0] # dir name
            if not path.exists(dir):
                mkdir(dir)
        if '/' in self.file:
            dir = self.file.split('/')[0] # dir Name
            if not path.exists(dir):
                mkdir(dir)
        if self.file.endswith('.html'):
            creatHTML(self.file) 
        elif self.file.endswith('.py'):
            creatPYTHON(self.file)
        else:
            createFile(" ", self.file)
            
    def touch0(self) -> None:
        """
        passing attribs to the writefile function
        """
        if self.file:
            self.writeFile() 
        elif self.files:
            for _ in self.files:
                self.file = str(_)
                self.writeFile()
    def execute(self):
        """
        this method makes decisions based on argvs.
        """
        if len(argv) == 1:
            print(TouchDoc)
        if '-v' in argv:
            print(v)
        elif len(argv) == 2 and '-v' not in argv:
            self.file = argv[1]
            self.touch0()
        elif len(argv) > 2:
            self.files = argv[1:]
        else:
            print(TouchDoc)
    def __repr__(self) -> str:
        return '<Command: touch>'


touch101 = touch() # Making the touch object
if __name__ == '__main__':
    touch101.execute()
    

