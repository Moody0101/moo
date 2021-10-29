from os import scandir
from itertools import chain
from sys import argv
dirs = [".\\oscommands", ".\\gitcommands", ".\\oscommands\\hashingCommands"]
name = argv[1]
files = list(chain.from_iterable([i.path for i in scandir(x) if "py" in i.name.split('.') and i.name == name] for x in dirs))
print(str(files[0]))