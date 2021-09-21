# adding and committing at the same time
from sys import argv
from os import system

addCommit: str = """
add-commit => adds files and commits in github
usage: add-commit {commitMsg}(required)
"""
class add_commit:
    def __init__(self) -> None:
        if len(argv) == 2:
            if argv[1] == "--help":
                print(addCommit)
            else:
                system("git -add -A")
                system("git commit -m \"{argv[1]}\"")
        
        else:
            print(addCommit)

add_commit()
