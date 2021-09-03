from shutil import copy
from os import getcwd, scandir
def copy2():
    # current = getcwd() + "\\" + "n.txt"
    # copy(current, "C:/Users/pc/Documents/pythonHH/moo")
    # print(current)
    print(list(scandir("../dist"))[0].name)
if __name__ == "__main__":
    copy2()