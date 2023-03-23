import os
import glob
size=input("enter K-mers size: we recomend it to be min=20 max=200\n")

while not(size<200 and size>20):
    size=input("ERROR in input\n the number you entered is out of range\n please reEnter\n")
	
#the flag for overlaping kmers. if the user choose y it asks for the size of the jump.
#if the user choose n it makes the jump to the kmers size.
#in any other case it put the size to be size of the kmers divide to 10.	
overlaping=raw_input("Do you want overlaping kmers? enter y/n" +"\n")
print overlaping
if overlaping=='y' or overlaping=='Y':
    jump=input("enter K-mers jump size: \n")
elif overlaping=='n' or overlaping=='N':
    jump=size
else:
    jump=size/10

for filename in glob.glob('*_PathogenGenomforQuery.fa'):
    g=1
    d=""
    my_file = open(filename,'r')
    file_contents = my_file.read()
    for i in range (0,len(file_contents),jump):
        d+=">k-" +str(g)+ "index:" +str(i) +":"+str(i+size)+"\n"
        d+=file_contents[i:i+size]+"\n"
        g+=1
    filename=filename.replace("GenomforQuery.fa","") 
    f1=open(str(size)+'K-mers_'+str(jump)+'jump_'+filename+'Blast.fa', 'w+')
    f1.write(d)
    f1.close()
    



