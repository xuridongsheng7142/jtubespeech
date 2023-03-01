#!/bin/bash

. path.sh

task=en
data_path=/home/xudong.wang/xdwang/corpus/jtubespeech/en/jtub1
nj_video=4

total_line_num=`cat $data_path/choose.csv | wc -l`
split_line_num=$((total_line_num / $nj_video ))
split -l $split_line_num $data_path/choose.csv $data_path/choose_split.csv
for f in $data_path/choose_split.csv*; do
  echo $f
  sed -i '1i\videoid,auto,sub' $f
  out_dir=`echo $f | sed 's/choose_split.//g'`
  mkdir -p $out_dir
  {
    python3 tools/download_video.py $task $f --outdir $out_dir
  } &
  sleep 20s;
done
wait
