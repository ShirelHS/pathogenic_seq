import os
import glob

for filename in glob.glob("*.*"):
    if (filename.endswith('.fa')==True or filename.endswith('.txt')==True) and filename.endswith('*FinalKmers.fa')==False:
        os.remove(filename)
        
