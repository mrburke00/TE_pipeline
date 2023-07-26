#!/bin/bash
experiment_name=$(cat /scratch/Shares/layer/workspace/devin_sra/TE_pipeline/config.yaml | shyaml get-value experiment_name)
data_dir=$(cat /scratch/Shares/layer/workspace/devin_sra/TE_pipeline/config.yaml | shyaml get-value data_dir)


input="data/"${experiment_name}"_sraRuns.txt"

peaks=("246")

#peaks=("$@")
for i in "${!peaks[@]}"; do
	echo "${peaks[i]}"	

	while read sra_example; do
		#echo "${sra_example}"

		input=$data_dir/insertion_"${peaks[i]}".bed"
		output=$data_dir/population_insertion_"${peaks[i]}".txt"

		echo "${sra_example}" >> $output

		bedtools intersect -a $data_dir/samples/"${sra_example}"/out.pass.vcf -b $input >> $output

	done <$input
	
done
