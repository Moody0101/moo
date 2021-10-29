from shutil import copy
from os import system
def install():
    fileName = str(input("Which file do you want to install:  "))
    destination = "C:/Program Files/MoodyCommands/dist"
    MOO = "C:/Users/pc/Documents/Production/Moo_0.0.1/dist"
        print(f'installing {fileName}...')
        system(f"pyinstaller --onefile {fileName}")
    except:
        print("""
it seems like something is not installed, use pip install pyinstaller, then try again
                """)
    try:
        print('installing the executable...')
        copy("./dist/" + fileName.split('.')[0] + ".exe", destination)
        copy("./dist/" + fileName.split('.')[0] + ".exe", MOO)

    except Exception as e:
        print("something went worng")
        print(e)
    exit()
if __name__ == '__main__':
    install()
