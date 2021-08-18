from sys import argv
from os import mkdir, path

if len(argv) < 2:
    print("""

    moo package for file manipulation and organization

    version: 0.0.1

    author: moody

    language: python.
    ===> for one file
    usage: touch <fileName>
    ===> for multiple files: 
    usage: touch <list of files saparated with space any files>
    """
    )
elif len(argv) == 2:
    fileName = str(argv[1])
    if '\\' in fileName:
        
        dir = fileName.split('\\')[0]
        if not path.exists(dir):
            mkdir(dir)
    if '/' in fileName:
        
        dir = fileName.split('/')[0]
        if not path.exists(dir):
            mkdir(dir)
    with open(fileName, 'w+') as f:
        f.write(' ')
elif len(argv) > 2:
    for _ in argv[1::]:
        fileName = str(_)
        if '\\' in fileName:   
            dir = fileName.split('\\')[0]
            if not path.exists(dir):
                mkdir(dir)
            with open(fileName, 'w+') as f:
                f.write(' ')
        elif '/' in fileName:   
            dir = fileName.split('/')[0]
            if not path.exists(dir):
                mkdir(dir)
            with open(fileName, 'w+') as f:
                f.write(' ')
        else:
            with open(fileName, 'w+') as f:
                f.write(' ')
