import os
import glob


findMaxFile=dict()
for filename in glob.glob("*FinalKmers.fa"):
    statinfo = os.stat(filename)
    findMaxFile[filename]=statinfo.st_size
    

maxFile=max(zip(findMaxFile.values(), findMaxFile.keys()))[1]

for filename in glob.glob("*.*"):
    if (filename.endswith('.fa')==True or filename.endswith('.txt')==True) and filename!=maxFile:
        os.remove(filename)
        
