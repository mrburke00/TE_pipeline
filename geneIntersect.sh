#!/bin/bash


if [ $# -eq 0 ]; then
    >&2 echo "No arguments provided"
    exit 1
fi

while getopts l:u:s:c: flag
do
    case "${flag}" in
	c) cluster=${OPTARG};;
        s) species=${OPTARG};;
        l) low=${OPTARG};;
        u) high=${OPTARG};;
    esac
done

output=output/"${species}"/peak_"${low}"-"${high}"/gcf_"${low}"-"${high}"_cluster"${cluster}".txt
input=output/"${species}"/peak_"${low}"-"${high}"/${species}_"${low}"-"${high}"_cluster"_${cluster}".txt

bedtools intersect -a data/${species}/${species}.gtf -b $input -wb > $output
