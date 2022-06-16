import sys, os

webmlist, txt_list, fix_webm, fix_txt = sys.argv[1:5]

id_dict = {}
with open(webmlist, 'r') as f:
    for line in f:
        id = os.path.basename(line.strip()).replace('.webm', '')
        id_dict[id] = line.strip()

txt_dict = {}
with open(txt_list, 'r') as f:
    for line in f:
        id = os.path.basename(line.strip()).replace('.txt', '')
        txt_dict[id] = line.strip()

fix_webm_count, fix_txt_count = "", ""
for key in id_dict.keys() & txt_dict.keys():
    fix_webm_count += id_dict[key] + '\n'
    fix_txt_count += txt_dict[key] + '\n'

with open(fix_webm, 'w') as f:
    f.write(fix_webm_count)

with open(fix_txt, 'w') as f:
    f.write(fix_txt_count)
