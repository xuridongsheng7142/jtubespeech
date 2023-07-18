#!/bin/bash

source activate whisper

nj_txt=100
nj_list=8
nj_video=4

task='de'
data_path=/home/xudong.wang/xdwang/corpus/asr/$task/jtub/1

search_word_txt=$data_path/word/$task/${task}wiki-latest-pages-articles-multistream-index.txt
video_id_txt=$data_path/videoid/${task}wiki-latest-pages-articles-multistream-index.txt

mkdir -p $data_path/tmp $data_path/videoid $data_path/sub

echo "step 1: get search word"
python3 scripts/make_search_word.py $task --outdir $data_path
cat $search_word_txt | sort -u > $data_path/word/$task/${task}wiki-latest-pages-articles-multistream-index_sort.txt
mv $data_path/word/$task/${task}wiki-latest-pages-articles-multistream-index_sort.txt $search_word_txt

echo 'step 2: get video id'
total_line_num=`cat $search_word_txt | wc -l`
split_line_num=$((total_line_num / $nj_txt ))
split -l $split_line_num $search_word_txt $data_path/tmp/${task}wiki-latest-pages-articles-multistream-index.txt
ls $data_path/tmp/${task}wiki-latest-pages-articles-multistream-index.txt* > $data_path/tmp/index.list
total_index_num=`cat $data_path/tmp/index.list | wc -l`

for((i=1;i<=$total_index_num;i++)); do
  mkdir -p $data_path/$i/videoid
  line=$(sed -n "${i}p" "$data_path/tmp/index.list")
  python3 tools/obtain_video_id.py $line $data_path/$i/videoid/${task}wiki-latest-pages-articles-multistream-index.txt
done

cat $data_path/*/videoid/${task}wiki-latest-pages-articles-multistream-index.txt | sort -u > $data_path/videoid/${task}wiki-latest-pages-articles-multistream-index.txt

echo 'step 3: get sub'
total_line_num=`cat $video_id_txt | wc -l`
if [ $total_line_num -gt 10000 ]; then
  rm $data_path/tmp/*
  for((i=1;i<=$total_index_num;i++)); do
    rm -r $data_path/$i
  done
else
  echo 'Video id is too short !!! Maybe something wrong here !!!'
  exit 1;
fi

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

if [ $task == 'tl' ]; then
  cat $data_path/*/sub/*/txt*/fil/${task}wiki-latest-pages-articles-multistream-index.csv  | grep -v 'videoid,auto,sub' > $data_path/sub/${task}wiki-latest-pages-articles-multistream-index.csv
else
  cat $data_path/*/sub/*/txt*/$task/${task}wiki-latest-pages-articles-multistream-index.csv | grep -v 'videoid,auto,sub' > $data_path/sub/${task}wiki-latest-pages-articles-multistream-index.csv
fi

cat $data_path/sub/${task}wiki-latest-pages-articles-multistream-index.csv | grep True$ > $data_path/sub/choose.csv
