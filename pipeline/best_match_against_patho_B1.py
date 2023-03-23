import numpy
import glob
indexFile=open("numOfPathogen.txt","r")
i=indexFile.read()
i=int(i)

CheckSeqArr=numpy.full((i), False, dtype=bool)
name=""
for filename in glob.glob('*vs_P_Blast1.txt'):
    my_file = open(filename,'r')
    kmerSize=filename.split("K")
    kmerSize=int(kmerSize[0])
    f1=open(filename+"_best_matches.txt",'w+')
    PredRow=[0]
    for line in my_file:
        row=line.split('\t')
        if not PredRow[0] ==row[0]:#its a new kamer
            if numpy.sum(CheckSeqArr) > (0.85*i):
                f1.write(PredRow[0])
                f1.write("\n")
                CheckSeqArr=numpy.full(i, False, dtype=bool)
        if float(row[2]) > 85 and float(row[3]) > kmerSize-int(kmerSize/4):
            CheckSeqArr[int(row[1])-1]=True
        PredRow=row    
    my_file.close()
    f1.close()
