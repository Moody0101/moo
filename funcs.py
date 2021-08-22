
from variables import PYTHON, HTML, doc


def doc():
    print(doc)


def createFile(content, fileName):
    open(fileName, 'w+').write(content)


def creatHTML(fileName):
    createFile(HTML, fileName)


def creatPYTHON(fileName):
    createFile(PYTHON, fileName)