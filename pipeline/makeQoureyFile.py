# -*- coding: utf-8 -*-
import os
import random
import glob
#for not pathogen



numOfGenomToBlast=input("Enter number of starts point, recommended between 2-5, Smaller = faster, larger = more accurate")



f=input("Enter the name of the pathogen directory:")
while not os.path.isdir(f):
    f=input(str(f)+" is not a dirctory. please reEnter")
i=1
randNumbers=[]
ofile = open("Pathogen_DB.fas", "w")
numOfPathoFiles=len(glob.glob(os.path.join(f,'*.fasta')))

#For a predefined number,
#select a random number in the range 
#between 0 and the number of pathogene sequences in dirctory,
# keeping all the numbers in a list, making sure there are no repetitions.
for t in range(numOfGenomToBlast):
    randomFileNum=random.randint(1,numOfPathoFiles)
    while(randomFileNum in randNumbers):
            randomFileNum=random.randint(1,numOfPathoFiles)
    randNumbers.append(randomFileNum)

for filename in glob.glob(os.path.join(f,'*.fasta')):
    my_file = open(filename)
    line=my_file.readline()
    if i in randNumbers:
        out=open(str(i)+"_PathogenGenomforQuery.fa","w")
        while(line):
                 if not line.startswith(">"):
                    line=line.strip()
                    out.write(line)
                 line=my_file.readline()
        ofile.write("\n\n")
    i+=1
indexFile=open("numOfPathogen.txt","w")
indexFile.write(str(i-1))
indexFile.close()

ofile.close()
out.close()
my_file.close()

