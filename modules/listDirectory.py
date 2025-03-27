import os

def listDirectory(filePath: str, targetParent: str):
    allFiles : list[str] = os.listdir(filePath)
    allDirectories : list = []
    for file in allFiles:
        dirFilePath = os.path.join(filePath, file)
        if os.path.isdir(dirFilePath):
            allDirectories.append(file)
    for dirName in allDirectories:
        if dirName == targetParent:
            allDirectories.remove(targetParent)
    return allDirectories