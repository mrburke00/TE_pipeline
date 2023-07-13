import yaml
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

with open('config.yaml', 'r') as file:
	config_args = yaml.safe_load(file)


sra_info_file = config_args['sra_info_file']
experiment_name = config_args['experiment_name']
vcf_file = 'data/vcf_merged_'+experiment_name+'.txt'
df = pd.read_csv(vcf_file, sep='\t', lineterminator='\n')
df.columns = ['chrom','start','end','length','seq','species']
df = df[df['length']!='.']
df['length'] = df['length'].astype(int)

x = df['length']

peaks, _ = find_peaks(x, height=0)

plt.plot(x)

plt.plot(peaks, x[peaks], "x")

plt.plot(np.zeros_like(x), "--", color="gray")

plt.show()
