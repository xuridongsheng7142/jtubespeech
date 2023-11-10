#!/bin/bash 

. path.sh 

task=de
result_path=/home/xudong.wang/xdwang/corpus/jtubespeech/$task/${task}_sub

#cat /home/xudong.wang/xdwang/results/wenet/German/add_jtub1/train/wav.scp | grep data4_29 > /home/xudong.wang/xdwang/results/wenet/German/add_jtub1/train/wav_jtb.scp
#python tools/data/get_utt.py /home/xudong.wang/xdwang/results/wenet/German/add_jtub1/train/wav_jtb.scp > $result_path/utt.list
#
#mkdir -p $result_path/vtts $result_path/txts
#
#python tools/data/down_vtt_only.py $result_path/utt.list $result_path/vtts $task
#
#find $result_path/vtts -name "*.vtt" > $result_path/vtts.list
#python tools/data/get_vtt2txt.py $result_path/vtts.list $result_path/txts $task
#find $result_path/txts -name "*.txt" > $result_path/txts.list
#python tools/data/get_txt2ref_mul.py $result_path/txts.list $result_path/ref.txt
#
#file_path=$result_path/ref.txt
#
#awk '{
#    for (i=2; i<=NF; i++) {
#        if ($i ~ /[0-9]/) {
#            print
#            break
#        }
#    }
#}' "$file_path" > $result_path/ref_num.txt

python tools/data/get_num2word_de.py $result_path/ref_num.txt $result_path/ref_num_fix.txt

bash tools/data/fil_num.sh $result_path/ref_num_fix.txt > $result_path/ref_num_todo.txt
fil_commen_id $result_path/ref_num_todo.txt $result_path/ref_num_fix.txt $result_path/ref_num_done.txt

python tools/data/get_ref_fil_task.py $result_path/ref_num_done.txt $task > $result_path/ref_num_done_fil.txt

python tools/data/check_diff.py $result_path/ref_num_done.txt $result_path/ref_num_done_fil.txt > $result_path/ref_num_diff.txt
