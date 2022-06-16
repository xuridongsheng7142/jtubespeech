#!/bin/bash

nj_txt=100
nj_list=8
nj_video=4

task=vi
result_path=/home/xudong.wang/xdwang/corpus/jtubespeech/Vietnamese/word_v2
org_path=$result_path/../word

#python tools/data/fil_sub.py $org_path/sub/split_100/merge.csv $org_path/videoid/viwiki-latest-pages-articles-multistream-index_sortu.txt > $result_path/videoid/${task}wiki-latest-pages-articles-multistream-index.txt

bash tools/retrieve_subtitle_exists_mul.sh $task $result_path $nj_txt $nj_list

exit 0;
bash tools/download_video_mul.sh $task $result_path $nj_video

