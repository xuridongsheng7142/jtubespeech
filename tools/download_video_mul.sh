#!/bin/bash

task=$1 
data_path=$2
nj_video=$3

result_video=$data_path/video/split_$nj_video

mkdir -p $result_video

#find $data_path/sub/* -name "${task}wiki-latest-pages-articles-multistream-index.csv" > $result_video/sub.list

total_line_num=`cat $result_video/sub.list | wc -l`
split_line_num=$((total_line_num / $nj_video ))
#split -l $split_line_num $result_video/sub.list $result_video/sub_list.list


for f in `ls $result_video/sub_list.list*`; do
  {
    i=0
    echo $f
    cat $f | while read line; do
      i=$((i+1))
      each_f=$line
      out_dir=$result_video/`echo $f | sed "s/.*\.//g"`_$i
      mkdir -p $out_dir
      echo $out_dir
      python tools/download_video.py $task $each_f --outdir $out_dir
    done
  } &
  sleep 1s;
done
wait
