import glob
indexFile=open("numOfKmersInDB.txt","r")
i=indexFile.read()
i=int(i)

flag=False
BlastResults = open("bestresultTest.txt",'r')
kmerSize=70
f1=open("TitleResults.txt",'w+')
PredRow=[0]
for line in BlastResults:
    row=line.split('\t')
    if not PredRow[0] ==row[0]:#its a new kamer
        if flag:
            f1.write(PredRow[0])
            f1.write("\n")
            flag=False
    if float(row[2]) > 95 and float(row[3]) > kmerSize*3/4:
        flag=True
    PredRow=row
BlastResults.close()
f1.close()
TitleFile = open("TitleResults.txt",'r')
kmersFile =open("resultQueryFile.fa","r")
out=open("RESULTS_SEQ.txt","w+")
line=kmersFile.readline()
name=TitleFile.readline()
title=""
title=">"+name
flag=False
while(line):
    if title==line:
        out.write(line)
        seq=kmersFile.readline()
        out.write(seq)
        name=TitleFile.readline()
        title=">"+name
    line=kmersFile.readline()
TitleFile.close()
kmersFile.close()
out.close()
