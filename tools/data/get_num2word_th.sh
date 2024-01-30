#!/bin/bash 

. path.sh 

task=th
result_path=/home/xudong.wang/xdwang/corpus/jtubespeech/$task/${task}_sub

cat $result_path/wav.scp | grep jtub > $result_path/wav_jtb.scp
python tools/data/get_utt.py $result_path/wav_jtb.scp > $result_path/utt.list

mkdir -p $result_path/vtts $result_path/txts

python tools/data/down_vtt_only.py $result_path/utt.list $result_path/vtts $task

find $result_path/vtts -name "*.vtt" > $result_path/vtts.list
python tools/data/get_vtt2txt.py $result_path/vtts.list $result_path/txts $task
find $result_path/txts -name "*.txt" > $result_path/txts.list
python tools/data/get_txt2ref_mul.py $result_path/txts.list $result_path/ref.txt

bash tools/data/fil_num.sh $result_path/ref.txt > $result_path/ref_num.txt
fil_file_by_utt2spk $result_path/wav_jtb.scp $result_path/ref_num.txt $result_path/ref_num_train.txt

python tools/data/get_num2word_th.py $result_path/ref_num_train.txt $result_path/ref_num_fix.txt

awk '{
    for (i=2; i<=NF; i++) {
        if ($i ~ /[a-zA-Z]/) {
            break
        }
        if (i == NF) {
            print
        }
    }
}' $result_path/ref_num_fix.txt > $result_path/ref_num_fix_fil_en.txt


bash tools/data/fil_num.sh $result_path/ref_num_fix_fil_en.txt > $result_path/ref_num_todo.txt
fil_commen_id $result_path/ref_num_todo.txt $result_path/ref_num_fix_fil_en.txt $result_path/ref_num_done.txt

python tools/data/get_ref_fil_task.py $result_path/ref_num_done.txt $task > $result_path/ref_num_done_fil.txt

python tools/data/check_diff.py $result_path/ref_num_done.txt $result_path/ref_num_done_fil.txt > $result_path/ref_num_diff.txt
