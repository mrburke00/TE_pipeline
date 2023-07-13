#!/bin/bash

animal="horse"

input="../sv_results/sra_runinfos/"${animal}"_sraRuns.txt"
home="/scratch/Shares/layer/workspace/devin_sra/sv_step/sv_results"

peaks=("246")

peaks=("$@")
for i in "${!peaks[@]}"; do
	echo "${peaks[i]}"
	

	for j in "${!sra_examples[@]}"; do
		echo "${sra_examples[j]}"
		echo "${sra_examples[j]}" >> v2output_sep1.txt

		input="output/"${peaks[i]}"/insertion_"${peaks[i]}".bed"
		output="output/"${peaks[i]}"/population_insertion_"${peaks[i]}".txt"
		bedtools intersect -a "${sra_examples[j]}"/out.pass.vcf -b $input >> $output

	done
	
done