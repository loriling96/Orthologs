from sys import argv
import re
#arguments = blastout, query fasta file, blastdb fasta file

aipgenes = []
querylist = []
genedict = {}
dscr_dict = {}
ev_dict = {}
#pattern = re.compile(r"\[.*\]")
printline = 0

#from blastoutput, filter out results with evalues greater than 1e-5, save aiptasia gene ids and matching query ids
blastout = open(argv[1])
for line in blastout:
	lsplit = line.strip().split()
	queryid, aipgeneid, evalue = lsplit[0], lsplit[1], float(lsplit[10])
	if queryid not in querylist:
		querylist.append(queryid)
	if evalue < 1e-5:
		if aipgeneid not in aipgenes:	
			aipgenes.append(aipgeneid)
			genedict[aipgeneid] = queryid
			ev_dict[aipgeneid] = evalue
		else:
			if ev_dict[aipgeneid] > evalue:
				genedict[aipgeneid] = queryid
				ev_dict[aipgeneid] = evalue
				 
blastout.close()

#from query fasta, get gene description to append to new aiptasia fasta line
queryfasta = open(argv[2])
for line in queryfasta:
	if line.startswith('>'):
		queryid = line.split(' ')[0][1:] #get query gene id, remove '>'
		querydescription = line.strip().split(' ')[1:]
		descriptionline = ' '.join(querydescription)
		dscr_dict[queryid] = descriptionline
queryfasta.close()

#extract hits from aiptasia fastafile
for q in querylist:
	dbfasta = open(argv[3])
	for line in dbfasta:
		if line.startswith('>'):
			aipgeneid = line.strip()[1:] #remove leading '>'
			if aipgeneid in aipgenes and genedict[aipgeneid] == q:
				print line.strip()+" "+genedict[aipgeneid]+" "+dscr_dict[genedict[aipgeneid]]
				printline = 1
				continue
			else:
				printline = 0	
		if printline:
			print line.strip()
	dbfasta.close()
		