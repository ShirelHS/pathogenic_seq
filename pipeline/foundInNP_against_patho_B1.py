import glob
identetyValue=85#defult, the user can modifed
kmersInNP=[]
for filename in glob.glob("*_vs_NP_Blast2.txt"):
    f=open(filename,"r")
    ksize=filename.split("K")
    ksize=int(ksize[0])
    outFileName=filename.split("blast2")[0]
    #f1=open(outFileName+"FoundInNP.txt","w")
    name=""
    flag=True
    for line in f:
        row=line.split("\t")
        if row[0]==name and flag==False:
            continue
        elif flag==False:
            flag=True
        if float(row[3])>(ksize*0.85) and float(row[2])>identetyValue and row[0] not in kmersInNP:
            #f1.write(row[0])
            #f1.write("\n")
            kmersInNP.append(row[0])
            flag=False
        name=row[0];


    bestMatchFileName=filename.replace("2.fa_vs_NP_Blast2.txt",".fa_vs_P_Blast1.txt_best_matches.txt")
    f3=open(bestMatchFileName,'r')
    resultsfileName=filename.replace("2.fa_vs_NP_Blast2","result")
    out=open(resultsfileName+".fa","w")
    for line in f3:
        row=line.split("\t")
        row[0]=row[0].strip()
        if not row[0] in kmersInNP:
            out.write(row[0]+"\n")
    f.close()
    #f1.close()
    f3.close()
    out.close()
    kmersInNP=[]

    

    
  



