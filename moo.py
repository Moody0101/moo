from sys import argv
from os import mkdir,path, remove
# from colors import colors


class commands:
    def __init__(self, fileName: str = None, files: list[str] = None) -> None:
        self.doc = f"""
    
    moo package for file manipulation and organization 
    
    version: 0.0.1

    author: moody

    language: python.   
    description:
    command line tool that clones the linux commands like touch, cat, and can delete a
    file or multiple files.
    

        flags: 
        --touch ==> create files with one touch.

        --cat ==> checking the content of a file.
        --delete ==> delete any file in any directory


        usage:
        
        moo <flag> fileName or a list of files but this works only in the touch and del
        command.
        so, in the cat flag, one file is is the only thing that should be specified
"""
        
        self.fileName = fileName
        self.files = files
    def docstring(self):
        print(self.doc)
    def touch0(self) -> None:
        if self.fileName:
            self.fileName = str(argv[1])
            if '\\' in self.fileName:
                dir = self.fileName.split('\\')[0]
                if not path.exists(dir):
                    mkdir(dir)
            if '/' in self.fileName:
                
                dir = self.fileName.split('/')[0]
                if not path.exists(dir):
                    mkdir(dir)
            with open(self.fileName, 'w+') as f:
                f.write(' ')
        elif self.files:
            for _ in self.files:
                Name = str(_)
                if '\\' in Name:   
                    dir = Name.split('\\')[0]
                    if not path.exists(dir):
                        mkdir(dir)
                    with open(Name, 'w+') as f:
                        f.write(' ')
                elif '/' in Name:   
                    dir = Name.split('/')[0]
                    if not path.exists(dir):
                        mkdir(dir)
                    with open(Name, 'w+') as f:
                        f.write(' ')
                else:
                    with open(Name, 'w+') as f:
                        f.write(' ')
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
        if len(argv) == 1:
            self.docstring()
        if '--touch' in argv:
            
            if len(argv) == 3:
                self.fileName = argv[2]
                print(self.fileName)
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
    def __repr__(self) -> str:
        return '<commands/>'         


if __name__ == '__main__':
    command = commands()
    command.execute()

