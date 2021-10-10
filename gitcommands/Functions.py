from subprocess import check_output
from os import pipe, system
from sys import argv

data, temp = pipe()
def getcommandOutput(command: str= "git branch") -> str: 
    return check_output(f"{command}", stdin=data, shell=True).decode("utf-8")

if __name__ == '__main__':
	system("cd ..")
	print(getcommandOutput(argv[1]))
	system("cd gitcommands")