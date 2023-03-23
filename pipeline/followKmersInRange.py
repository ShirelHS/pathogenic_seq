import re
import glob
Range=input("enter Range Size For overlapping Kmers:")
for filename in glob.glob('*FinalKmers.fa'):
    resultsFilhendle=open(filename ,"r")
    title1=resultsFilhendle.readline()
    kmer1=resultsFilhendle.readline()
    helper1= map(int,re.findall('\d+', title1 ))
    strartIndex1=helper1[1]
    endIndex1=helper1[2]
    flag=True
    newResult=open("PerKmersOverlappingInRange.fa","w")
    while not title1 is None:
        helper1= map(int,re.findall('\d+', title1 ))
        strartIndex1=helper1[1]
        endIndex1=helper1[2]
        title2=resultsFilhendle.readline()
        kmer2=resultsFilhendle.readline()
        helper2= map(int,re.findall('\d+', title2 ))
        if helper2==[]:
            break
        strartIndex2=helper2[1]
        endIndex2=helper2[2]
        if not(strartIndex2 > endIndex1) and (endIndex2-strartIndex1) < Range :
            p=title1+kmer1+title2+kmer2
            newResult.write(p)
            newResult.write("\n")
        title1=title2
        kmer1=kmer2

     




