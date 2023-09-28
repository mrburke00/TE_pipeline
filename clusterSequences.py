import argparse
from Bio import pairwise2


argParser = argparse.ArgumentParser()
argParser.add_argument("-l", "--low", help="low peak bp size")
argParser.add_argument("-u", "--high", help="high peak bp size")
argParser.add_argument("-s", "--species", help="species/experiment name")
argParser.add_argument("-p", "--pid", help="minimum pid threshold")

args = argParser.parse_args()

if args.high is None or args.low is None or args.species is None:
	print("missing arguments")
	exit()

midpoint = (int(args.low) + int(args.high))/2

if args.pid is None:
	args.pid = 0.9 * midpoint
else:
	args.pid =  args.pid * midpoint


bed_input_file = 'output/'+args.species+'/peak_'+args.low+'-'+args.high + '/'+args.species+'_'+args.low+'-'+args.high+'_pop_vcf.txt'


entries = []
coords = []
with open(bed_input_file) as f:
	lines = f.readlines()
	for i in range(len(lines)):
		entries.append(lines[i])

all_clusters = []
all_coords = []
remaining_sequences = entries.copy()

for i,X in enumerate(remaining_sequences):
	#start = time.time()
	cluster = []
	cluster_coords = []
	X_seq = X.split()[-2]
	for j,Y in enumerate(remaining_sequences):
		Y_seq = Y.split()[-2]
		alignments = pairwise2.align.globalxx(X_seq, Y_seq)

	if float(alignments[0].score) >= 180:
		cluster.append(Y)
		del remaining_sequences[j]
        
	if len(cluster) > 0:
		all_clusters.append(cluster)
		#all_coords.append(cluster_coords)
		#end = time.time()
		#print(end - start,len(remaining_sequences))
    
	if len(remaining_sequences) < 10000:
		break

for i,cluster in enumerate(all_clusters):
	output_file = 'output/'+args.species+'/peak_'+args.low+'-'+args.high+'/'+args.species+'_'+args.low+'-'+args.high+'_cluster_'+str(i)+'.txt'
	with open(output_file, 'w') as r:
		for c in cluster:
			r.write(c)

remaining_file = 'output/'+args.species+'/peak_'+args.low+'-'+args.high+'/'+args.species+'_'+args.low+'-'+args.high+'_cluster_remaining_sequences.txt'
with open(remaining_file, 'w') as r:
	for c in remaining_sequences:
		r.write(c)
