from sys import argv, version
from os import mkdir,path, remove
from funcs import doc, createFile, creatHTML, creatPYTHON
from variables import v
class commands:
    def __init__(self, fileName: str = None, files: list[str] = None) -> None:
        self.fileName = fileName
        self.files = files
    def writeFile(self):
        if '\\' in self.fileName:
            dir = self.fileName.split('\\')[0]
            if not path.exists(dir):
                mkdir(dir)
        if '/' in self.fileName:
            dir = self.fileName.split('/')[0]
            if not path.exists(dir):
                mkdir(dir)
        if self.fileName.endswith('.html'):
            creatHTML(self.fileName)      
        elif self.fileName.endswith('.py'):
            creatPYTHON(self.fileName)
        else:
            createFile(" ", self.fileName)
            
    def touch0(self) -> None:
        if self.fileName:
            self.writeFile() 
        elif self.files:
            for _ in self.files:
                self.fileName = str(_)
                self.writeFile()
    def cat(self) -> None:
        content = open(self.fileName, 'r').read()
        print(f"""
    {content}
    """)
    def delete(self):
        if self.fileName:
            remove(self.fileName)
        elif self.files:
            for _ in self.files:
                remove(_)
    def execute(self) -> None:
        if '--version' in argv:
            print(v)
            exit()
        if '--touch' in argv:
            if len(argv) == 3:
                self.fileName = argv[2]
                self.touch0()
            elif len(argv) > 2:
                self.files = argv[2::]
                self.touch0()
        elif '--cat' in argv:
            self.fileName = argv[2]
            self.cat()
        elif '--delete' in argv:
            if len(argv) == 2:
                print('the file to be removed has not yet been specified!!')
            elif len(argv) == 3:
                self.fileName = argv[2]
            elif len(argv) > 3:
                self.files = argv[2::]
            self.delete()
        else:
            doc()
    def __repr__(self) -> str:
        return '<commands/>' 


if __name__ == '__main__':
    command = commands()
    command.execute()

