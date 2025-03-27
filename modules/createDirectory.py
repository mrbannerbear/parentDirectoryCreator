import os

def createDirectory(filePath: str, dirName: str):
    # could use f"{filePath}\{dirName}" but ''\' is used in windows only, macOS uses '/' 
    # so directory variable is used for cross-platform support (os.path.join(...))
    directory = os.path.join(filePath, dirName)
    isDirExists : bool = os.path.exists(directory)
    if not isDirExists:
        os.mkdir(directory)
        isDirExists = True
    return directory