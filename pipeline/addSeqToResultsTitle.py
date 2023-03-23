import glob
for filename in glob.glob("*PathogenBlastresult.txt.fa"):
    ResultsTitleFile=open(filename,"r")
    KmersFile=open (filename.split("result")[0]+".fa","r")
    FinaleKamers=open(filename.split("B")[0]+"FinalKmers.fa","w")
    kmer=KmersFile.readline()
    for line in ResultsTitleFile:
        if line.startswith("k"):
            line=">"+line
            while not kmer==line:
                kmer=KmersFile.readline()
            seq= KmersFile.readline()
            FinaleKamers.write(kmer)
            FinaleKamers.write(seq)
    ResultsTitleFile.close()
    KmersFile.close()
    FinaleKamers.close()
