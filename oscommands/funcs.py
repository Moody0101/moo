
from variables import PYTHON, HTML, documentation, CPP
from os import mkdir

def doc():
    print(documentation)


def createFile(content, fileName):
    try:
        with open(fileName, 'w+') as f:
            f.write(content)
    except:
        try:
            mkdir('/'.join(fileName.split('/')[:-1]))
        except:
            mkdir('\\'.join(fileName.split('\\')[:-1]))
        createFile(content, fileName)




def creatHTML(fileName):
    createFile(HTML, fileName)



def creatPYTHON(fileName):
    createFile(PYTHON, fileName)


def creatCPP(fileName):
    createFile(CPP, fileName)

