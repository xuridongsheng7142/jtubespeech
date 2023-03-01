#!/bin/bash

# jtub2  jtub3
#nj_txt=100
#nj_list=8
#nj_video=4
#
#task=th
#result_path=/data/dczheng/data/thai/thai_jtube/video/th/wav
#save_path=/data/xdwang/data4_29/xdwang/datas/asr/th/jtub3
#
#mkdir -p $save_path/data $save_path/wavs
#
##find $result_path -name "*webm" > $save_path/data/webm.list
##find $result_path/../txt -name "*.txt" > $save_path/data/txt.list
#
##python tools/data/mp4towav_16k.py $save_path/data/webm.list $save_path/wavs
#
#find $save_path/wavs_16k -name "*.wav" > $save_path/data/wavs_16k.list
#python3 tools/data/get_Thai_data_mul.py $save_path/data/wavs_16k.list $save_path/data/txt.list $save_path/data/ref.txt $save_path/wavs_split 


# jtub4
task=th
data_path=/data/xdwang/data4_29/xdwang/datas/asr/th/jtub4/data
save_path=/data/xdwang/data4_29/xdwang/datas/asr/th/jtub4
nj_video=8

export PATH=$PWD:/usr/local/bin:$PATH

#grep "True$" $data_path/alluniqth_sub > $data_path/choose.csv
#
#total_line_num=`cat $data_path/choose.csv | wc -l`
#split_line_num=$((total_line_num / $nj_video ))
#split -l $split_line_num $data_path/choose.csv $data_path/choose_split.csv
#for f in $data_path/choose_split.csv*; do
#  echo $f
#  sed -i '1i\videoid,auto,sub' $f
#  out_dir=`echo $f | sed 's/choose_split.//g'`
#  mkdir -p $out_dir
#  {
#    python3 tools/download_video.py $task $f --outdir $out_dir
#  } &
#  sleep 20s;
#done
#wait

#find $data_path -name "*webm" > $data_path/webm.list
#find $data_path -name "*.txt" > $data_path/txt.list
#
#python tools/data/mp4towav_16k.py $data_path/webm.list $save_path/wavs
#
#find $save_path/wavs_16k -name "*.wav" > $save_path/data/wavs_16k.list
#python3 tools/data/get_Thai_data_mul.py $save_path/data/wavs_16k.list $save_path/data/txt.list $save_path/data/ref.txt $save_path/wavs_split
#
#exit 0;

## jtub5
#nj_txt=100
#nj_list=8
#nj_video=4
#
#task=th
#data_path=/data/xdwang/data4_29/xdwang/datas/asr/th/jtub5
#nj_video=8
#
#bash tools/retrieve_subtitle_exists_mul.sh $task $data_path $nj_txt $nj_list

nj_video=8

data_path=/home/xudong.wang/xdwang/corpus/jtubespeech/Thai/jtub5
save_path=/home/xudong.wang/xdwang/data4_29/xdwang/datas/asr/th/jtub5
task=th

#total_line_num=`cat $data_path/choose.csv | wc -l`
#split_line_num=$((total_line_num / $nj_video ))
#split -l $split_line_num $data_path/choose.csv $data_path/choose_split.csv
#for f in $data_path/choose_split.csv*; do
#  echo $f
#  sed -i '1i\videoid,auto,sub' $f
#  out_dir=`echo $f | sed 's/choose_split.//g'`
#  mkdir -p $out_dir
#  {
#    python3 tools/download_video.py $task $f --outdir $out_dir
#  } &
#  sleep 20s;
#done
#wait

#mkdir -p $data_path/data
#
#find $data_path -name "*webm" > $save_path/data/webm.list
#find $data_path -name "*.txt" > $save_path/data/txt.list
#
#python tools/data/mp4towav_16k.py $save_path/data/webm.list $save_path/wavs
#
#find $save_path/wavs_16k -name "*.wav" > $save_path/data/wavs_16k.list
#python3 tools/data/get_Thai_data_mul.py $save_path/data/wavs_16k.list $save_path/data/txt.list $save_path/data/ref.txt $save_path/wavs_split
#

save_path=/home/xudong.wang/xdwang/corpus/jtubespeech/Thai/jtub5_sub

python tools/data/mp4towav_16k.py $save_path/data/webm.list $save_path/wavs

find $save_path/wavs_16k -name "*.wav" > $save_path/data/wavs_16k.list
python3 tools/data/get_Thai_data_mul.py $save_path/data/wavs_16k.list $save_path/data/txt.list $save_path/data/ref.txt $save_path/wavs_split
