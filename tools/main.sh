#!/bin/bash

nj_txt=100
nj_list=8
nj_video=4

task=vi
result_path=/home/xudong.wang/xdwang/corpus/jtubespeech/Vietnamese/word
save_path=/home/xudong.wang/xdwang/data1_29/xdwang/ASR_Data/Vietnamese/train_data/jtubespeech/1

#python scripts/make_search_word.py $task --outdir $result_path
#python tools/obtain_video_id.py $result_path/word/$task/${task}wiki-latest-pages-articles-multistream-index.txt $result_path/videoid/${task}wiki-latest-pages-articles-multistream-index.txt
#
#bash tools/retrieve_subtitle_exists_mul.sh $task $result_path $nj_txt $nj_list

#bash tools/download_video_mul.sh $task $result_path $nj_video

find $result_path/video -name "*webm" > $save_path/data/webm.list
find $result_path/video -name "*.txt" > $save_path/data/txt.list

python tools/data/mp4towav_16k.py $save_path/data/webm.list $save_path/wavs

#find $save_path/wavs_16k -name "*.wav" > $save_path/data/wavs_16k.list
#python3 tools/data/get_Vietnamese_data_mul.py $save_path/data/wavs_16k.list $save_path/data/txt.list $save_path/data/ref.txt $save_path/wavs_split 
