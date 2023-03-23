import os
import glob

sizes=[50,100,150,200,250,300,350,400]
jumps=[5,10,15,20,25,30,35,40]

for k in range(8):
    for filename in glob.glob('*_PathogenGenomforQuery.fa'):
        g=1
        d=""
        my_file = open(filename,'r')
        file_contents = my_file.read()
        for i in range (0,len(file_contents),jumps[k]):
            d+=">k-" +str(g)+ "index:" +str(i) +":"+str(i+sizes[k])+"\n"
            d+=file_contents[i:i+sizes[k]]+"\n"
            g+=1
        filename=filename.replace("GenomforQuery.fa","") 
        f1=open(str(sizes[k])+'K-mers_'+str(jumps[k])+'jump_'+filename+'Blast.fa', 'w+')
        f1.write(d)
        f1.close()
                
