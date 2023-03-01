import sys, os
import re
import multiprocessing
import logging

txt_list, ref_txt = sys.argv[1:3]

def get_one_ref(line):
    count = ''
    fs = 16000
    text_path = line.strip()
    utt = os.path.basename(text_path).replace(".txt", "")
    with open(text_path, 'r') as f:
        for line_t in f:
            if len(line_t.strip().split('\t')) == 3:
                start_time, end_time, ref = line_t.strip().split('\t')
                char_to_save = re.findall(pattern, ref)
                if float(end_time) - float(start_time) >= 2 and len(char_to_save) > 0 and float(end_time) - float(start_time) <= 30:
                    start_point = int(float(start_time) * fs)
                    end_point = int(float(end_time) * fs)
                    each_data_name = utt + "_" + str(start_point) + "_" + str(end_point)
                    each_ref = ''.join([char for char in ref if char in char_to_save])
                    count += each_data_name + ' ' + each_ref + '\n'
    return count

def pasrse_page(x):
    if x != None and x != "\n":
        with open(ref_txt,'a') as f:
            f.write(x)

pattern = re.compile(r"[\u0E00-\u0E7F']")

if os.path.exists(ref_txt): os.remove(ref_txt)

with open(txt_list, "r") as f:
    lines = f.readlines()

#for line in lines:
#    get_one_ref(line)

print("Start get data split, please wait !")
cc = multiprocessing.cpu_count()
proc_pool = multiprocessing.Pool(int(cc/8))

for line in lines:
    if ' ' in line: data_path = line.strip().split(" ")[1]
    else: data_path = line.strip()
    proc_pool.apply_async(get_one_ref, args=(data_path,), callback=pasrse_page)

proc_pool.close()
proc_pool.join()
print("All subprocesses done.")
