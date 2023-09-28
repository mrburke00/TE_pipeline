import argparse
import pandas as pd
import re

argParser = argparse.ArgumentParser()
argParser.add_argument("-l", "--low", help="low peak bp size")
argParser.add_argument("-u", "--high", help="high peak bp size")
argParser.add_argument("-s", "--species", help="species/experiment name")
argParser.add_argument("-c", "--cluster_no", help="cluster number")


args = argParser.parse_args()

if args.high is None or args.low is None or args.species is None or args.cluster_no is None:
	print("missing arguments")
	exit()

meta_data_file = 'data/'+args.species+'/'+args.species+'_meta.csv'

bed_input_file = 'output/'+args.species+'/peak_'+args.low+'-'+args.high + '/'+args.species+'_'+args.low+'-'+args.high+'_cluster'+'_'+args.cluster_no+'.txt'
gcf_annotated_file = 'output/'+args.species+'/peak_'+args.low+'-'+args.high + '/'+args.species+'_gcf_'+args.low+'-'+args.high+'_cluster'+'_'+args.cluster_no+'.txt'
loci_annotated_file = 'output/'+args.species+'/peak_'+args.low+'-'+args.high + '/'+args.species+'_loci_'+args.low+'-'+args.high+'_cluster'+'_'+args.cluster_no+'.txt'

print(gcf_annotated_file)

with open(gcf_annotated_file) as f:
    with open(loci_annotated_file, 'w') as w:
        lines = f.readlines()
        for line in lines:
            #print(name = re.search('gene_id (.*); gene_version', line).group(1))
            try:
                #name = re.search('gene_name (.*); gene_source', line).group(1)
                name = re.search('gene_id (.*); gene_version', line).group(1)
                name =  name.strip('"')
                line = line.split(';')
                s = line[-1:][0].split()
                s = s[0] + '\t' + s[1] + '\t' + s[2] + '\t' + s[4]
                int_type = line[0].split()[2]
                w.write(s + '\t' + name + '\t' + int_type +'\n')
            except:
                pass
            try:
                #name = re.search('gene_id (.*); gene_version', line).group(1)
                name = re.search('gene_id (.*); gene_version', line).group(1)
                name =  name.strip('"')
                line = line.split(';')
                s = line[-1:][0].split()
                s = s[0] + '\t' + s[1] + '\t' + s[2] + '\t' + s[4]
                int_type = line[0].split()[2]
                w.write(s + '\t' + name + '\t' + int_type +'\n')
            except:
                continue

meta_data = pd.read_csv(meta_data_file, sep='\t')
meta_data=meta_data.dropna(axis=1, how='all')
meta_data=meta_data.dropna(axis=0, how='all')

if len(meta_data.columns) > 2:
    meta_data = meta_data.drop(meta_data.columns[2:len(meta_data.columns)], axis=1)
print(meta_data)
meta_data.columns = ['sra','breed']


df = pd.read_csv(loci_annotated_file, sep='\t', comment='t', header=None)
header = ['chrom', 'chromStart', 'chromEnd','sname', 'gene', 'type']
df.columns = header[:len(df.columns)]

breed_names = []
for idx, row in df.iterrows():
    breed_names.append(meta_data.loc[meta_data['sra'] == row['sname']]['breed'].values[0])
df['breed_name'] = breed_names

df_counts = df.groupby(['breed_name'])['gene'].value_counts().unstack()
gene_names = []
sums = []
for col in df_counts.columns:
    if df_counts[col].sum() > 1:
        gene_names.append(col)
        sums.append(df_counts[col].sum())

print(sums)
print(*gene_names, sep = ' ')
print(df_counts)
