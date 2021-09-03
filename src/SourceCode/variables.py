v: str = 'moo: 0.0.1'

documentation: str = """
    moo package for file manipulation and organization 
    
    version: 0.0.1

    author: moody

    language: python.   
    description:
    command line tool that clones the linux commands like touch, cat, and can delete a
    file or multiple files.
    

    flags: 
        --touch ==> create files with one touch.
        Example:
            moo --touch main.py ==> creates a file called main.py
            but if you want to make more than one file, then use this command
            moo --touch main.py main.js main.c main.html ==> creates more than one file with the specified names
        
        --cat ==> checking the content of a file.
        Example:
            moo --cat main.py ==> displays the content of the main.py 
        --delete ==> delete any file in any directory
        Example:
            moo --delete main.py ==> deletes the main.py file
            note ==> (it does not delete dirs)
            moo --delete main.py main.js ==> deletes every specified file.
"""
# starter code 

HTML: str = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel=\"stylesheet\" href=\"\">
    <script src=\"\"></script>
</head>


<body>

</body>

</html>         
"""
PYTHON: str = """
class Name:

    def __init__(self):
        pass


def main():

    instance = Name()



if __name__ == '__main__':
    main()

"""