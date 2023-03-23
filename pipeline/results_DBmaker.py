import random
import glob
import os
flag=True

dbResults=""
for filename in glob.glob('*FinalKmers.fa'):  
    my_file = open(filename)
    if flag:
	resultQueryFile=my_file.read()
	fout=open("resultQueryFile.fa","w")
	fout.write(resultQueryFile)
	fout.close()
        flag=False
        continue
    tag=filename.split("Final")[0]
    tag=tag.split("s")[1]
    for line in my_file:
        if line.startswith(">"):
	   line=line.replace("\n","")
	   line=line+tag+"\n"
        dbResults+=line
    
ofile=open("ResultsDB.fa","w")
ofile.write(dbResults)
ofile.close()
indexFile=open("numOfKmersInDB.txt","w")
nline=dbResults.count('\n')
indexFile.write(str(nline))
indexFile.close()





