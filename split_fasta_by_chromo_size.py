#!/usr/bin/env python
# coding: utf-8
# Label split_fasta_by_chromo_size
#author rachid elfermi
#contact rachid.elfermi@gmail.com
# version 1.0
# usage python3 split_fasta_by_chromo_size.py inputfile  output_path approximated_number_of_file
sequencescoton = {}
countercoton=[]
count=0
ids=[]
allid=[]
jj=0
descr = None
plant=sys.argv[1]
out_path=sys.argv[2]
number_of_files=sys.argv[3]
size=int(os.stat(plant).st_size/number_of_files)
with open(plant,"r") as file:
    line = file.readline()[:-1] # always trim newline
    while line:
        if line[0] == '>':
            if descr: # any sequence found yet?
                sequencescoton[descr]= seq
                countercoton.append((len(seq),descr))
            descr = line[1:].split()[0]
            seq = '' # start a new sequence
        else:
            seq += line
        line = file.readline()[:-1]
    sequencescoton[descr]= seq
    countercoton.append((len(seq),descr))
for ind,val in enumerate(countercoton):
    count+=val[0]
    ids.append(val[1])
    if count>=size:
        jj+=1
        with open(f"{out_path}/{plant}_{jj}.fa","w") as fp:
            for NC in  set(ids):
                fp.write(f">{NC}\n")
                fp.write(f"{sequencescoton[NC]}\n") 
        count=0
        allid+=ids
        ids=[]
    elif count<size and ind==len(countercoton)-1:
        allid+=ids
        jj+=1
        with open(f"{test_res}/{plant}_{jj}.fa","w") as fp:
            for NC in  set(ids):
                fp.write(f">{NC}\n")
                fp.write(f"{sequencescoton[NC]}\n") 

