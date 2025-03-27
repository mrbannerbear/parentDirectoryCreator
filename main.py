from modules.createDirectory import createDirectory
from modules.nameInputs import directoryName
from modules.listDirectory import listDirectory
from modules.moveDirectory import moveDirectory

def main():
    filePath: str = r"C:\Users\pc\OneDrive\Desktop"
    dirName: str =  "deskParentDir"
    # dirName: str = directoryName()
    newParentDirectoryPath = createDirectory(filePath=filePath, dirName=dirName)
    allDirectories : list[str] = listDirectory(filePath=filePath, targetParent=dirName)
    moveDirectory(directoriesToBeMoved=allDirectories, source=filePath, destination=newParentDirectoryPath)

main()