# pathogenic_seq

This pipeline is finding common genomics elements for one population that are not shared by another, based on multiple comparisons. 
It generates primers for the result sequences.

This pipeline uses blast, primer3 and its runing on python and bash.

To activate this pipeline run "Pathogen_pipline" bash script.

In order to run the pipeline the user should provide 2 directories:
1. A directory of sequences of of a population that the query is about sharing common genomics elements. 
2. A directory of sequences of another population. 

The pipeline asks the user for some parameters in order to run, like length of k-mer and etc.
