import scipy.io.wavfile as wav_func
import numpy as np
import sys, os
import re
import multiprocessing
import logging

logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')

def get_one_wav_split(wav_path):
    wav_name = os.path.basename(wav_path).replace(".wav", "")
    count = ''
    if wav_name in utt_dict:
        logging.info('{}'.format(wav_path))
        fs, data = wav_func.read(wav_path)
        with open(utt_dict[wav_name], 'r') as f_t:
            for line_t in f_t:
                if len(line_t.strip().split('\t')) == 3:
                    start_time, end_time, ref = line_t.strip().split('\t')
                    char_to_save = re.findall(pattern, ref)
                    if float(end_time) - float(start_time) >= 2 and len(char_to_save) > 0 and float(end_time) - float(start_time) <= 30:
                        start_point = int(float(start_time) * fs)
                        end_point = int(float(end_time) * fs)
                        each_data = data[start_point:end_point]
                        each_data_name = wav_name + "_" + str(start_point) + "_" + str(end_point)
                        each_ref = result_string = ''.join([char for char in ref if char in char_to_save])
                        count += each_data_name + ' ' + each_ref + '\n'
                        save_data = data_root_path + '/' + each_data_name + '.wav'
                        if not os.path.exists(save_data):
                            wav_func.write(save_data, fs, each_data)
        return count 

def pasrse_page(x):
    if x != None and x != "\n":
        with open(ref_txt,'a') as f:
            f.write(x)

wavlist = sys.argv[1]
textlist = sys.argv[2]
ref_txt = sys.argv[3]
data_root_path = sys.argv[4]

if not os.path.exists(data_root_path): os.makedirs(data_root_path)
if os.path.exists(ref_txt): os.remove(ref_txt)

utt_dict = {}
with open(textlist, "r") as f:
    for line in f:
        text_path = line.strip()
        utt = os.path.basename(text_path).replace(".txt", "")
        utt_dict[utt] = text_path

pattern = re.compile(r"[\u0E00-\u0E7F']")

with open(wavlist, "r") as f:
    lines = f.readlines()

#for line in lines:
#    data_path = line.strip()
#    get_one_wav_split(data_path)
#exit(0)

print("Start get data split, please wait !")
cc = multiprocessing.cpu_count()
proc_pool = multiprocessing.Pool(int(cc/8))

for line in lines:
    if ' ' in line: data_path = line.strip().split(" ")[1]
    else: data_path = line.strip()
    proc_pool.apply_async(get_one_wav_split, args=(data_path,), callback=pasrse_page)

proc_pool.close()
proc_pool.join()
print("All subprocesses done.")
