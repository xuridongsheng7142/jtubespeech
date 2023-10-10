import sys, os

textlist, ref_txt = sys.argv[1:3]

fs = 16000
rm_str_list = ['&nbsp', '&lt', '&gt', '&amp']

count = ''
with open(textlist, "r") as f:
    for line in f:
        text_path = line.strip()
        utt = os.path.basename(text_path).replace(".txt", "")
        with open(text_path, 'r') as ff:
            for line_t in ff:
                if len(line_t.strip().split('\t')) == 3:
                    start_time, end_time, ref = line_t.strip().split('\t')
                    for rm_s in rm_str_list:
                        ref = ref.replace(rm_s, '')
                    start_point = int(float(start_time) * fs)
                    end_point = int(float(end_time) * fs)
                    each_data_name = utt + "_" + str(start_point) + "_" + str(end_point)
                    count += each_data_name + ' ' + ref + '\n'
                else:
                    print('bad line:', line_t.strip())

with open(ref_txt, 'w') as f:
    f.write(count)

