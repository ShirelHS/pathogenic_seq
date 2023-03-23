import os
import glob

for filename in glob.glob("*.txt_best_matches.txt"):
    TitleFile = open(filename,'r')
    kmersFilename=filename.split("_vs")
    kmersFilename= kmersFilename[0]
    print kmersFilename
    kmersFile =open(kmersFilename,'r')
    kmerSize=filename.split("K")
    kmerSize=int(kmerSize[0])
    outFileName=(filename.split(".fa")[0])+"2.fa"
    out=open(outFileName,"w+")
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
 






