from os import system
from sys import argv


def main():
    # g++ -o hello <= fileTocompileto> hello.cpp <= the input file>
    if len(argv) == 2:
        fileName = argv[1]
        out = fileName.split('.')[0]
        ext = fileName.split('.')[1]
        if ext != "cpp":
            print("The specified file is not a c++ file")
        else:
            system(f"g++ -o {out} {fileName} && {out}")
    else:
        print("""
usage: cc <c++FileName/>
""")
if __name__ == '__main__':
    main()