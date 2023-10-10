#!/bin/bash

. path.sh

task=fil
data_path=/home/xudong.wang/xdwang/corpus/jtubespeech/tl/1
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

mkdir -p $data_path/data

find $data_path -name "*.wav" | grep wav16k > $data_path/data/wavs_16k.list
find $data_path -name "*.txt" > $data_path/data/txt.list
python3 tools/data/get_filipino_data_mul.py $data_path/data/wavs_16k.list $data_path/data/txt.list $data_path/data/ref.txt $data_path/wavs_split

find $data_path/wavs_split -name "*.wav" > $data_path/data/wavs_split.list
