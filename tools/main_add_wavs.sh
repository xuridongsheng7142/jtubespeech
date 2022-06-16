#!/bin/bash

nj_txt=100
nj_list=8
nj_video=4

task=vi
result_path=/home/xudong.wang/xdwang/corpus/jtubespeech/Vietnamese/word
save_path=/home/xudong.wang/xdwang/data1_29/xdwang/ASR_Data/Vietnamese/train_data/jtubespeech/2
org_path=/home/xudong.wang/xdwang/data1_29/xdwang/ASR_Data/Vietnamese/train_data/jtubespeech/1

mkdir -p $save_path/data

#find $result_path/video -name "*webm" > $save_path/data/webm_all.list
#find $result_path/video -name "*.txt" > $save_path/data/txt_all.list

#python tools/data/fil_webm.py $org_path/data/webm.list $save_path/data/webm_all.list > $save_path/data/webm.list
#python tools/data/fil_webm.py $org_path/data/txt.list $save_path/data/txt_all.list > $save_path/data/txt.list

#python tools/data/get_commen_id.py $save_path/data/webm.list $save_path/data/txt.list $save_path/data/webm_fil.list $save_path/data/txt_fil.list

#mv $save_path/data/webm_fil.list $save_path/data/webm.list
#mv $save_path/data/txt_fil.list $save_path/data/txt.list

#python tools/data/mp4towav_16k.py $save_path/data/webm.list $save_path/wavs

#find $save_path/wavs_16k -name "*.wav" > $save_path/data/wavs_16k.list
python3 tools/data/get_Vietnamese_data_mul.py $save_path/data/wavs_16k.list $save_path/data/txt.list $save_path/data/ref.txt $save_path/wavs_split 
