import yaml
import pandas as pd 
import numpy as np 
import subprocess

with open('config.yaml', 'r') as file:
	config_args = yaml.safe_load(file)


sra_info_file = config_args['sra_info_file']
experiment_name = config_args['experiment_name']
vcf_file = 'data/vcf_merged_'+experiment_name+'.txt'
df = pd.read_csv(vcf_file, sep='\t', lineterminator='\n')
df.columns = ['chrom','start','end','length','seq','species']
df = df[df['length']!='.']
df['length'] = df['length'].astype(int)



def writeFasta(df_peak, output_file):
	with open(output_file, 'w') as f:
		for i,row in df_peak.iterrows():
		    coords = '>'+str(row['chrom'])+':'+str(row['start'])+'-'+str(row['end'])
		    #coords = '>'+str(row['chrom'])+':'+str(row['start'])+'-'+str(row['end'])

		    f.write(coords)
		    f.write('\n')
		    f.write(row['seq'])
		    f.write('\n')


def writeBed(fasta_file, bed_file):
	entries = []
	with open(fasta_file) as f:
	    with open(bed_file, 'w') as r:
	        lines = f.readlines()
	        for line in lines:
	            line = line.split()
	            if ">" in line[0]:
	                t = line[0].split(":")
	                chrom = t[0].strip(">")
	                start = t[1].split("-")[0]
	                end = t[1].split("-")[0]
	                #spec = t[1].split("?")[1]
	                #r.write(chrom + '\t' + start + '\t' + end + '\t' + spec + '\n')
	                r.write(chrom + '\t' + start + '\t' + end + '\n')



#assume we have peaks right now 
#will add functionality for bandwidth of peak	    
peaks = [246]

#need to specify species in output
bashCommand = "mkdir -p output"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

for peak in peaks:
	bashCommand = 'mkdir -p output/'+str(peak)
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

	df_peak = df[(df['length'] >= int(peak)) & (df['length'] <= int(peak))]
	df_peak = df_peak[df_peak['length']!='.']
	df_peak = df_peak.drop_duplicates(subset=['chrom','start','end'], keep='first')

	fasta_file = 'output/'+str(peak)+'/insertion_'+str(peak)+'.txt'
	bed_file =  'output/'+str(peak)+'/insertion_'+str(peak)+'.bed'
	writeFasta(df_peak, fasta_file)
	writeBed(fasta_file, bed_file)




