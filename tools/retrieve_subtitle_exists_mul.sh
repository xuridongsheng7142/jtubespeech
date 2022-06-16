#!/bin/bash 

task=$1
data_path=$2
nj_txt=$3
nj_txtlist=$4

video_id_txt=$data_path/videoid/${task}wiki-latest-pages-articles-multistream-index.txt
video_id_split=$data_path/videoid/split_$nj_txt 
video_list_split=$data_path/videoid/split_$nj_txtlist
result_split=$data_path/sub/split_$nj_txt

mkdir -p $video_id_split $video_list_split

total_line_num=`cat $video_id_txt | wc -l`
split_line_num=$((total_line_num / $nj_txt ))
split -l $split_line_num $video_id_txt $video_id_split/${task}wiki-latest-pages-articles-multistream-index.txt

find $video_id_split/${task}wiki-latest-pages-articles-multistream-index.txt* > $video_id_split/video_id.list

total_line_num=`cat $video_id_split/video_id.list | wc -l`
split_line_num=$((total_line_num / $nj_txtlist ))
split -l $split_line_num $video_id_split/video_id.list $video_list_split/video_id.list


for f in `ls $video_list_split/video_id.list*`; do
  {
    echo $f
    cat $f | while read line; do
      each_f=$line
      out_dir=$result_split/`echo $each_f | sed "s/.*\.//g"`
      mkdir -p $out_dir
      echo $out_dir
      python scripts/retrieve_subtitle_exists.py $task $each_f --outdir $out_dir
    done
  } & 
  sleep 1s;
done
wait

