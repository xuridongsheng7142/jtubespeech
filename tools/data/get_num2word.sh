
result_path=/home/xudong.wang/xdwang/corpus/jtubespeech/fr/fr_sub
task=fr

#cat /home/xudong.wang/xdwang/results/wenet/French/add_jt1_2/train/wav.scp | grep jtubespeech > /home/xudong.wang/xdwang/results/wenet/French/add_jt1_2/train/wav_jtb.scp
#python tools/data/get_utt.py /home/xudong.wang/xdwang/results/wenet/French/add_jt1_2/train/wav_jtb.scp  > $result_path/utt.list

mkdir -p $result_path/vtts $result_path/txts

python tools/data/down_vtt_only.py $result_path/utt.list $result_path/vtts $task

find $result_path/vtts -name "*.vtt" > $result_path/vtts.list
python tools/data/get_vtt2txt.py $result_path/vtts.list $result_path/txts $task
find $result_path/txts -name "*.txt" > $result_path/txts.list
python tools/data/get_txt2ref.py $result_path/txts.list $result_path/ref.txt

file_path=$result_path/ref.txt

awk '{
    for (i=2; i<=NF; i++) {
        if ($i ~ /[0-9]/) {
            print
            break
        }
    }
}' "$file_path" > $result_path/ref_num.txt
