import os
import glob

for filename in glob.glob("*PathogenBlastresult.txt.fa"):
    TitleFile = open(filename,'r')
    partFileName=filename.split("PathogenBlastresult.txt")[0]
    writeKmers=open(partFileName+"Final_Kmers.txt",'w')
    kmersFile=open(partFileName+"PathogenBlast2.fa",'r')
    flag=False
    KfindNP=TitleFile.read()
    for line in kmersFile:
        if flag==True:
            writeKmers.write(line)
            flag=False
        if line.startswith('>')==True:
            num=line.split('k')
            print KfindNP
            print num
            if num[1] in KfindNP:
                print num[1]
                writeKmers.write(line)
                flag=True
    TitleFile.close()
    writeKmers.close()
    kmersFile.close()
