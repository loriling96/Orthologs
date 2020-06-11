# script to create a clean file of Aipgene and Nematostella orthologs compatible with STRING database
# written specifically for UBH_output.txt from Masa's UBH_e.py script and formatted for input into my STAMSmapping.R script
# ignores the UBH if a match pair already exists in dictionary. 
# only works because the input file was already sorted for A<->B matches before the UBH matches


Usage= "cleanNematostellaID.py inputUBHlist outputUBH"
import sys
import re

if len(sys.argv) < 3:
    print(Usage)

infile, outfile = sys.argv[1:]

def write_report(r, filename):    
    with open(filename, "w") as input_file:
        for k, v in r.items():
            input_file.write('%s\t%s\n'%(k,v))
            #input_file.write(k+'\t'+v+'\n')
            
            """
            line = '{}, {}'.format(k, v) 
            print(line, file=input_file)
            """

#RBH_dict={} #create empty dictionary
UBH_dict={}

with open(infile, mode ='rU') as F1:
    header=F1.readline()
    header2=F1.readline()
    for line in F1:
        ls=line.strip().split()
        A_id, B_id = ls[0], ls[1]
        #print(A_id,'\t', B_id)
        N_id=A_id.split('|')[3]
        #print(N_id),sys.exit()
        if B_id not in UBH_dict:
            UBH_dict[B_id]=N_id #write dictionary with aipgene name as key in brackets and Nematostella ID as values
        else:
            continue


#save dictionary to file
#file2='/Users/lorraineling/Documents/Pringlelab/Aip_Nem_Orthologs/Aip_Nem_RBH3.filt.txt'
write_report(UBH_dict, outfile)
