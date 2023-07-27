import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
import seaborn as sns 
import random
from sklearn.decomposition import PCA
import string
from sklearn.preprocessing import StandardScaler
import yaml

with open('config.yaml', 'r') as file:
	config_args = yaml.safe_load(file)


sra_info_file = config_args['sra_info_file']
data_dir = config_args['data_dir']
experiment_name = config_args['experiment_name']
vcf_file = 'data/vcf_merged_'+experiment_name+'.txt'
multibreed_study = config_args['multibreed_study']
                       
                       
df = pd.read_csv(vcf_file, sep='\t', lineterminator='\n')
df.columns = ['chrom','start','end','length','seq','species']
df = df[df['length']!='.']
df['length'] = df['length'].astype(int)

#assume we have peaks right now 
#will add functionality for bandwidth of peak	    
peaks = [246]                       
        
if not multibreed_study: # use SRA number as identifier
    print('yes')
    for peak in peaks:
        peak_dir =  data_dir + '/peaks/' + str(peak) + '/'
        
        fasta_file = peak_dir + 'insertion_'+str(peak)+'.txt'
        bed_file =  peak_dir + 'insertion_'+str(peak)+'.bed'  
        
        population_peak_file = peak_dir + 'population_insertion_'+str(peak)+'.txt'  
        
        # get all loci for peak
        entries = []
        with open(bed_file) as f:
            lines = f.readlines()
            for line in lines: #
                line = line.split()
                end = int(line[1]) + int(line[2])
                t = ">"+line[0]+":"+line[1]+"-"+str(line[1])
                entries.append(t)
                
        meta_data = pd.read_csv(sra_info_file)
        meta_data=meta_data.dropna(axis=1, how='all')
        meta_data=meta_data.dropna(axis=0, how='all')
        meta_data.columns = ['sra']
        
        samples = {}

        with open(population_peak_file) as f:
            lines = f.readlines()
            for line in lines:
                if "output" in line: 
                    sample_name = line.split('/')[1].strip() 
                    #if sample_name in meta data 
                        #samples[sample_name] = np.zeros(len(entries)) 
                #else:
                    #t = line.split()
                    #chrom = t[0]
                    #start = t[1]
                    #end = start
                    #seq = re.search('SVINSSEQ=(.*);SPLIT_READS',line)
                    #seq = seq.group(1)
                    #s = ">"+chrom+":"+start+"-"+end
                    #if s in entries and chrom not in  ['X', 'Y']:#check which SV in ref to TE loci 
                        #idx = entries.index(s)
                        #samples[sample_name][idx] = 1