from Functions import getcommandOutput
from json import dumps, load
from os import path, system, mkdir, pipe
from sys import argv
from collections import deque
from subprocess import check_output

usage: str = """
usage:
    only run this command in the main dir of your repository gitPush
    and everything else will be figured out automatically
"""

class gitpush:

    def __init__(self, remote, branch) -> None:
            self.remote, self.branch  = remote, branch
    def push(self):
        print("""
----------------------------------***Pushing into github**-----------------------------------
            """)
        try:
            system(f'git push {self.remote}  {self.branch}')
        
        except Exception as e:
            print(e)
        print("""
-----------------------------------------------------------------------------------------
            """)

    def execute(self):
        if len(argv) == 1:
            self.branch = getcommandOutput()[2:]
            self.remote = getcommandOutput("git remote")
            self.push()
        elif len(argv) > 1:
            if len(argv) == 2:
                if argv[1] == '--version' or argv[1] == '-v':
                    print(usage)
                else:
                    self.remote = argv[1]
                    self.push()
            elif len(argv) == 3:
                self.remote = argv[1]
                self.branch = argv[2]
                self.push()


def main():

    instance = gitpush()
    instance.execute()
if __name__ == '__main__':
    main()

