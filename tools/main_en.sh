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
source activate whisper

nj_txt=100
nj_list=8
nj_video=4

task=en
result_path=/home/xudong.wang/xdwang/corpus/asr/en/jtub

#python3 scripts/make_search_word.py $task --outdir $result_path
#python3 tools/obtain_video_id.py $result_path/word/$task/${task}wiki-latest-pages-articles-multistream-index.txt $result_path/videoid/${task}wiki-latest-pages-articles-multistream-index.txt
#
#cp $result_path/videoid/${task}wiki-latest-pages-articles-multistream-index.txt $result_path/videoid/${task}wiki-latest-pages-articles-multistream-index_back.txt
#cat $result_path/videoid/${task}wiki-latest-pages-articles-multistream-index_back.txt | sort -u > $result_path/videoid/${task}wiki-latest-pages-articles-multistream-index.txt

bash tools/retrieve_subtitle_exists_mul.sh $task $result_path $nj_txt $nj_list

exit 0;
bash tools/download_video_mul.sh $task $result_path $nj_video

find $result_path/video -name "*webm" > $save_path/data/webm.list
find $result_path/video -name "*.txt" > $save_path/data/txt.list

python tools/data/mp4towav_16k.py $save_path/data/webm.list $save_path/wavs

#find $save_path/wavs_16k -name "*.wav" > $save_path/data/wavs_16k.list
#python3 tools/data/get_Vietnamese_data_mul.py $save_path/data/wavs_16k.list $save_path/data/txt.list $save_path/data/ref.txt $save_path/wavs_split 
