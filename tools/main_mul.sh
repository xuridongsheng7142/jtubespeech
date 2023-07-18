#!/bin/bash

. path.sh

nj_txt=100
nj_list=8
nj_video=4

task=fr
data_path=/data2/xdwang/ASR_Data/French/train_data/jtubespeech/3_2
video_id_txt=$data_path/${task}wiki-latest-pages-articles-multistream-index.txt

mkdir -p $data_path/tmp

total_line_num=`cat $video_id_txt | wc -l`
split_line_num=$((total_line_num / $nj_txt ))
split -l $split_line_num $video_id_txt $data_path/tmp/${task}wiki-latest-pages-articles-multistream-index.txt
ls $data_path/tmp/${task}wiki-latest-pages-articles-multistream-index.txt* > $data_path/tmp/index.list
total_index_num=`cat $data_path/tmp/index.list | wc -l`

for((i=1;i<=$total_index_num;i++)); do
  mkdir -p $data_path/$i/videoid
  line=$(sed -n "${i}p" "$data_path/tmp/index.list")
  [ -f $line ] && mv $line $data_path/$i/videoid/${task}wiki-latest-pages-articles-multistream-index.txt
  bash tools/retrieve_subtitle_exists_mul.sh $task $data_path/$i $nj_txt $nj_list
done
