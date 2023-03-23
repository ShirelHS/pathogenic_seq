# -*- coding: utf-8 -*-
import os
import random
import glob

#A flag in order to find maximum results or not
flagMaxResults=raw_input("Do you want the maximum results or not? enter y/n \n")
maxResults = open("flag_max_results.txt", "w")
maxResults.write(flagMaxResults)
maxResults.close()

#for pathogen
fpatho=raw_input("Enter the name of the pathogen directory:\n")
while not os.path.isdir(fpatho):
    fpatho=input(str(fpatho)+" is not a dirctory. please reEnter")

#for not pathogen
i=1
f=raw_input("Enter the name of the not pathogen directory:\n")
#while not os.path.isdir(f):
#    f=input(str(f)+" is not a dirctory. please reEnter")

if flagMaxResults=='y' or flagMaxResults=='Y':
    numOfGenomToBlast=1
else: #if the choice is any other option but 'y'.
    numOfGenomToBlast=input("Enter number of starts point, recommended between 2-5, Smaller = faster, larger = more accurate\n")
    if not(numOfGenomToBlast<6 and numOfGenomToBlast>0):
        print("ERROR in input\n number of starts point=3 ,by default")
        numOfGenomToBlast=3
ofile = open("Not_Pathogen_DB.fas", "w")
for filename in glob.glob(os.path.join(f,'*')):  
    my_file = open(filename)
    line=my_file.readline()
    ofile.write(">"+str(i)+"\n")
    while(line):
        if not line.startswith(">"):
            line=line.strip()
            ofile.write(line)
        line=my_file.readline()
    ofile.write("\n\n")
    i=i+1   
ofile.close()
indexFile=open("numOfNotPathogen.txt","w")
indexFile.write(str(i-1))
indexFile.close()

#for pathogen
i=1
randNumbers=[]
ofile = open("Pathogen_DB.fas", "w")
numOfPathoFiles=len(glob.glob(os.path.join(fpatho,'*')))

#For a predefined number,
#select a random number in the range 
#between 0 and the number of pathogene sequences in dirctory,
# keeping all the numbers in a list, making sure there are no repetitions.
for t in range(numOfGenomToBlast):
    randomFileNum=random.randint(1,numOfPathoFiles)
    while(randomFileNum in randNumbers):
            randomFileNum=random.randint(1,numOfPathoFiles)
    randNumbers.append(randomFileNum)

for filename in glob.glob(os.path.join(fpatho,'*')):
    my_file = open(filename)
    line=my_file.readline()
    ofile.write(">"+str(i)+"\n")
    if i in randNumbers:
        out=open(str(i)+"_PathogenGenomforQuery.fa","w")
        while(line):
                 if not line.startswith(">"):
                    line=line.strip()
                    ofile.write(line)
                    out.write(line)
                 line=my_file.readline()
        ofile.write("\n\n")
    else:
          while(line):
                 if not line.startswith(">"):
                    line=line.strip()
                    ofile.write(line)
                 line=my_file.readline()
          ofile.write("\n\n")
    i+=1
indexFile=open("numOfPathogen.txt","w")
indexFile.write(str(i-1))
indexFile.close()

ofile.close()
out.close()
my_file.close()

