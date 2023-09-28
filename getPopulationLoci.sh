#!/bin/bash

if [ $# -eq 0 ]; then
    >&2 echo "No arguments provided"
    exit 1
fi

while getopts l:u:s: flag
do
    case "${flag}" in
        s) species=${OPTARG};;
        l) low=${OPTARG};;
        u) high=${OPTARG};;
    esac
done

#input="horse_246_cluster_0.bed"
#peak="240"

#sra_examples=("$@")
sra_numbers="data/"${species}"/"${species}"_sraRuns.txt"
data_dir="/scratch/Shares/layer/workspace/devin_sra/repeat_masker/local/src/INSurVeyor"
#mkdir output/"${species}"/
#mkdir output/"${species}"/peak_"$low"-"$high"/

#rm  output/"${species}"/peak_"$low"-"$high"/output_seqs.vcf
rm test.vcf


#for i in "${!sra_examples[@]}"; do
while read sra_example;	do
        echo output/"${sra_example}"

        #bcftools view -i  'SVLEN>='${low}' && SVLEN<='${high}'' $data_dir/output/"${sra_example}"/out.pass.vcf -o output/"${species}"/peak_"$low"-"$high"/output_seqs.vcf
	
	bedtools intersect -header -a $data_dir/output/"${sra_example}"/out.pass.vcf -b 1374_loci.txt -wb > test.vcf

        bcftools query -f '%CHROM\t%POS\t%INFO/END\t%SVINSSEQ\t'${sra_example}'\n' test.vcf >> pop_loci.txt

        rm test.vcf


done <$sra_numbers


##!/bin/bash
#experiment_name=$(cat /scratch/Shares/layer/workspace/devin_sra/TE_pipeline/config.yaml | shyaml get-value experiment_name)
#data_dir=$(cat /scratch/Shares/layer/workspace/devin_sra/TE_pipeline/config.yaml | shyaml get-value data_dir)


#input="data/"${experiment_name}"_sraRuns.txt"

#peaks=("246")

#peaks=("$@")
#for i in "${!peaks[@]}"; do
#	echo "${peaks[i]}"	

#	while read sra_example; do
#		#echo "${sra_example}"

#		input=$data_dir/insertion_"${peaks[i]}".bed"
#		output=$data_dir/population_insertion_"${peaks[i]}".txt"

#		echo "${sra_example}" >> $output

#		bedtools intersect -a $data_dir/samples/"${sra_example}"/out.pass.vcf -b $input >> $output

#	done <$input
	
#done
