from modules.createDirectory import createDirectory
from modules.nameInputs import directoryName

def main():
    filePath: str = r"C:\Users\pc\OneDrive\Desktop"
    # dirName: str =  "deskParentDir"
    dirName: str = directoryName()
    createDirectory(filePath=filePath, dirName=dirName)

main()