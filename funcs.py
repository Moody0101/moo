
from variables import PYTHON, HTML, documentation


def doc():
    print(documentation)


def createFile(content, fileName):
    open(fileName, 'w+').write(content)


def creatHTML(fileName):
    createFile(HTML, fileName)


def creatPYTHON(fileName):
    createFile(PYTHON, fileName)