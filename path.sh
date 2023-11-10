
ffmpeg_path=/home/xudong.wang/xdwang/tools/ffmpeg/ffmpeg-git
git_lfs_path=/data2/xdwang/anaconda/anaconda3/lib/python3.10/site-packages/git_lfs
export PATH=$ffmpeg_path:$git_lfs_path:$PWD:$PATH

function fil_file_by_utt2spk {
  utt2spk_=$1
  file=$2
  filed_file=$3
  cat $file | awk -v f1=$utt2spk_ 'BEGIN{while((getline<f1)>0)id_class[$1]=1; }
  {if ($1 in id_class) print $0}' | sort > $filed_file
}

function fil_commen_id {
  commen_id_list=$1
  file=$2
  filed_file=$3
  cat $file | awk -v f1=$commen_id_list 'BEGIN{while((getline<f1)>0)id_class[$1]=1; }
  {if ($1 in id_class);else print $0}' | sort > $filed_file
}
