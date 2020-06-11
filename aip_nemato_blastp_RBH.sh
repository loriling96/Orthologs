#!/bin/bash -eu

###the "-eu" are parameters to bash. "e" will make bash stop if there's an error. "u" will make bash stop if there's an undefined variable
### This will perform two reciprocol blastp searches of genome A and genome B, then it will run the RBH pyton script.

#$ -N reciprocol_blast

#specifies the maximum run time for X hours using 6GB of memory
#$ -l h_rt=6:00:00
#$ -l s_rt=6:00:00
#$ -l h_vmem=6G

# sends  email when job ends or aborts
#$ -m ea
#$ -M loriling@stanford.edu

#sets the path for saving the standard output stream and the standard error stream
#$ -o /home/loriling/logs
#$ -e /home/loriling/logs
#$ -w e
#$ -V
#$ -pe shm 2 

module load blast/2.2.29+
echo "aiptasia_nematostella_blastpRBH"
echo "Sol $(date)"



blastp -query ../../../../srv/gsfs0/projects/pringle/Lori/aiptasia.genome-models.aa.fa -db ../../../../srv/gsfs0/projects/pringle/Lori/Nematostella_protein_seq.fa -out ../../../../srv/gsfs0/projects/pringle/Lori/Aip_Nem_Orthologs/A_vs_N_blastpout.txt -outfmt 6 -evalue 1e-5 -num_alignments 5 &
blastp -query ../../../../srv/gsfs0/projects/pringle/Lori/Nematostella_protein_seq.fa -db ../../../../srv/gsfs0/projects/pringle/Lori/aiptasia.genome-models.aa.fa -out ../../../../srv/gsfs0/projects/pringle/Lori/Aip_Nem_Orthologs/N_vs_A_blastpout.txt -outfmt 6 -evalue 1e-5 -num_alignments 5
#wait
#module load python/3.4

#echo "Blast ran without issue. Python RBH is running!"
#python ../../../../srv/gsfs0/projects/pringle/Phil/Python_scripts/RBH.py ../../../../srv/gsfs0/projects/pringle/Lori/Aip_Nem_Orthologs/A_vs_N_blastpout.txt ../../../../srv/gsfs0/projects/pringle/Lori/Aip_Nem_Orthologs/N_vs_A_blastpout.txt 1 2 12 high ../../../../srv/gsfs0/projects/pringle/Lori/Aip_Nem_Orthologs/A_N.hits.out

