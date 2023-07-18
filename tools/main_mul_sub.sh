#!/bin/bash

. path.sh

nj_txt=100
nj_list=8
nj_video=4

task=en
data_path=/data3/xdwang/datas/asr/en/jtub2_3
choose_csv=$data_path/choose.csv

mkdir -p $data_path/tmp

total_line_num=`cat $choose_csv | wc -l`
split_line_num=$((total_line_num / $nj_txt ))
split -l $split_line_num $choose_csv $data_path/tmp/choose.csv
ls $data_path/tmp/choose.csv* > $data_path/tmp/csv.list
total_index_num=`cat $data_path/tmp/csv.list | wc -l`

for((i=1;i<=$total_index_num;i++)); do
  mkdir -p $data_path/$i
  line=$(sed -n "${i}p" "$data_path/tmp/csv.list")
  mv $line $data_path/$i/choose.csv
  bash tools/main_en_download.sh $data_path/$i
done
