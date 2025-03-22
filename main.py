from modules.createDirectory import createDirectory

def main():
    filePath: str = r"C:\Users\pc\OneDrive\Desktop"
    dirName: str =  "deskParentDir"
    createDirectory(filePath=filePath, dirName=dirName)

main()