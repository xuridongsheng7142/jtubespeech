import multiprocessing
import subprocess
import sys, os

def download_video(id, savepath, lang='vi'):
    save_f = "%s/%s.%s.vtt" % (savepath, id, lang)
    if not os.path.exists(save_f):
        command = f"yt-dlp --skip-download -o '{savepath}/%(id)s.%(ext)s' --write-subs --sub-lang {lang} https://www.youtube.com/watch?v={id}"
        subprocess.call(command, shell=True)

id_list, savepath, lang = sys.argv[1:4]

# 读取ID列表文件
with open(id_list, 'r') as file:
    id_list = file.readlines()

# 清除每行末尾的换行符
id_list = [id.strip() for id in id_list]

# 创建进程池
num_processes = 8
pool = multiprocessing.Pool(processes=num_processes)

# 使用进程池并行下载视频
pool.starmap(download_video, [(id, savepath, lang) for id in id_list])

# 关闭进程池
pool.close()
pool.join()

