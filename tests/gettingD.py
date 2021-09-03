from os import getcwd

def main():
    drive: str = '\\'.join([getcwd().split("\\")[0], 'users', 'pc', 'Program Files'])
    print(drive) 
    print(getcwd() + '\\')

if __name__ == '__main__':
    main()
    