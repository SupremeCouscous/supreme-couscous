import glob
import os

PATH1 = "c:\\windows"
PATTERN1 = "*\\*.dll"
alldlls = os.path.join(PATH1, PATTERN1)
for d in glob.glob(alldlls):
    print(d)