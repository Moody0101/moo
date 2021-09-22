from json import dumps, load
from os import path, system, mkdir
from sys import argv
from collections import deque


usage: str = """

gitToken [--store] [--get] [--token]

if you want to get your tokens then use this structur:
    gitToken --get
    ex: gitToken --get
    outputs:
        <Token> -----> <exprDate>
if you want to store a token then pass these args:
    gitToken --store <token> <expirationDate>
    ex: gitToken --store hdihgstzfqjdvdgvswbzau687865678 "sunday dec, 22 2021"
    Note: you better type the date inside quotation marks.

"""


class Token_:

    def __init__(self):
        self.the_set = dumps({'token': [], 'exp': []})
        self.dir = "c:/users/pc/documents/data"
        self.JsonPath = "c:/users/pc/documents/data/data.json"
        self.check_()
    def check_(self):
        if not path.exists(self.dir):
            mkdir(self.dir)
        if not path.isfile(self.JsonPath):

            open(self.JsonPath, 'x').write(self.the_set)
            print("made file")
        else:
            pass
        
        system(f"attrib {self.JsonPath} +H")
    def secureDB(self):
        if not path.exists(self.JsonPath):
            print("db does not exist")
            exit()
        system(f"attrib {self.JsonPath} +H")
    def clearDB(self):
        with open(self.JsonPath, 'w+') as f:
            f.write(self.the_set)
            print('cleared successfully!!')
    def openDb(self):
        system(f"attrib {self.JsonPath} -H")
    def storeData(self):
        if path.exists(self.JsonPath):
            data0 = load(open(self.JsonPath, 'r+'))['token']
            ddata0 = deque(data0)
            ddata0.appendleft(argv[2])
            data1 = load(open(self.JsonPath, 'r+'))['exp']
            ddata1 = deque(data1)
            ddata1.appendleft(argv[3])
            all_data = dumps({
                    'token': list(ddata0),
                    'exp': list(ddata1)
                    })
            open(self.JsonPath, 'w+').write(all_data)
        else:
            
            open(self.JsonPath, 'w+').write(self.the_set)
            self.storeData()
    def getData(self):
        if path.exists(self.JsonPath):
            i = 0        
            for _ in load(open(self.JsonPath, 'r'))['token']:
                print(f"{_}", " ===> expires at :", load(open(self.JsonPath, 'r'))['exp'][int(i)])
                i += 1
        else:
            print("it looks like there is Nothing to display")
            print()
            print("You can store using:\n gitToken --store <token> <expirationDate>")
    def execute(self):
        if len(argv) == 1:
            print(usage)
        elif len(argv) > 1:
            if argv[1] == "--get":
                self.getData()
            elif argv[1] == "--store":
                if len(argv) < 4:
                    print("seems like you forgot typing some required args")
                    print(usage)
                else:
                    self.storeData()
            elif argv[1] == "--clear":
                self.clearDB()
            elif argv[1] == "--version":
                print('a part of the moo package v: 0.0.1')
            else:
                print(usage)
        else:
            print(usage)

def main():

    tkn = Token_()
    tkn.openDb()
    tkn.execute()
    tkn.secureDB()

if __name__ == '__main__':
    main()
