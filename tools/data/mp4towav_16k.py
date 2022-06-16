import sys, os
import multiprocessing

def raw2wav(raw_path):
    wav_name = os.path.basename(raw_path).replace('.mp4', '.wav').replace('.webm', '.wav')
    final_wav = wav_root_path + "/" + wav_name
    final_wav_16k =  final_wav.replace('/wavs/', '/wavs_16k/') 
    if not os.path.exists(final_wav_16k):
        os.system("ffmpeg -nostdin -i %s %s" % (raw_path, final_wav))
        os.system("sox %s -c 1 -b 16 -r 16000 %s" % (final_wav, final_wav_16k))
        os.remove(final_wav)

if len(sys.argv) <= 2:
    print("Usage:\n\tpython tools/data/raw2wav.py raw_list wav_path")
    exit(1)

raw_list = sys.argv[1]
wav_root_path = sys.argv[2]

wav_16k_path = wav_root_path.replace("/wavs", "/wavs_16k")

if not os.path.exists(wav_root_path):
    os.makedirs(wav_root_path)

if not os.path.exists(wav_16k_path):
    os.makedirs(wav_16k_path)

with open(raw_list, "r") as f:
    lines = f.readlines()

print("Start change raw to wavs, please wait !")
cc = multiprocessing.cpu_count()
proc_pool = multiprocessing.Pool(int(cc/16))

for line in lines:
    raw_path = line.strip()
    proc_pool.apply_async(raw2wav, args=(raw_path,))

proc_pool.close()
proc_pool.join()
print("All subprocesses done.")
