import sys, os, re
from multiprocessing import Pool

textlist, ref_txt = sys.argv[1:3]

fs = 16000
rm_str_list = ['&nbsp', '&lt', '&gt', '&amp']
replace_dict = {"’": "'"}

def remove_punctuation(text):
    # 删除词尾的标点
    words = text.split()
    clean_words = [word.strip('.,;:!?').strip() for word in words if word.rstrip('.,;:!?')]
    clean_text = ' '.join(clean_words)
    return clean_text

def process_line(line):
    text_path = line.strip()
    utt = os.path.basename(text_path).replace(".txt", "")
    count = ''
    with open(text_path, 'r') as ff:
        for line_t in ff:
            if len(line_t.strip().split('\t')) == 3:
                start_time, end_time, ref = line_t.strip().split('\t')
                for rm_s in rm_str_list:
                    ref = ref.replace(rm_s, '')
                for key, value in replace_dict.items():
                    ref = ref.replace(key, value)
                ref = remove_punctuation(ref)
                ref = ref.replace(':', ' ')
                start_point = int(float(start_time) * fs)
                end_point = int(float(end_time) * fs)
                each_data_name = utt + "_" + str(start_point) + "_" + str(end_point)
                count += each_data_name + ' ' + ref + '\n'
            else:
                print('bad line:', line_t.strip())
    return count

with open(textlist, "r") as f:
    lines = f.readlines()

with Pool(processes=int(16)) as pool:
    results = pool.map(process_line, lines)
    count = ''.join(results)

with open(ref_txt, 'w') as f:
    f.write(count)

