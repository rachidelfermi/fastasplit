# fastasplit
this scripts splits fasta file into even approximated size without breaking a  any sequence 
usage python3 split_fasta_by_chromo_size.py inputfile  output_path approximated_number_of_file

the size for spliting the fasta file is chosen like this
size = size_of_inputfile / approximated_number_of_file
you can change it to a fixed size by changing the line 
size=int(os.stat(plant).st_size/number_of_files)
to
size=30000000 if you want file of 30MB 
