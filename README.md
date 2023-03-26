# pathogenic_seq

This pipeline is finding pathogenic islands on known pathogenic bacterias DNA, using multiple DNA comparisons. 
It generates primers for the result sequences.

This pipeline uses blast, primer3 and its runing on python and bash.

To activate this pipeline run "Pathogen_pipline" bash script.

In order to run the pipeline the user should provide 2 directories:
1. A directory of sequences of pathogenic bacteria from the same family. 
2. A directory of non-pathogenic sequences of bacteria from the same family (of the pathogenic bacteria). 

The pipeline asks the user for some parameters in order to run, like length of k-mer and etc.
