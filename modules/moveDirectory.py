import shutil
import os

def moveDirectory(directoriesToBeMoved : list[str], source: str, destination: str):
    try:
        for dir in directoriesToBeMoved:
            dirPath = os.path.join(source, dir)
            shutil.move(dirPath, destination)
        print("Success!")
    except:
        print("An error occurred")