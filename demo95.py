import os

PATH1 = "c:/windows/system32"

for currentFolder, subFolders, fileNames in os.walk(PATH1):
    print(f"under {currentFolder}")
    print(f"***** {subFolders}")
    for f in fileNames:
        print(f"----->{f}")
    pass