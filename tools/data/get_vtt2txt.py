import sys, os
sys.path.append('./')
from scripts.util import make_video_url, make_basename, vtt2txt, autovtt2txt

vtt_list, save_path, lang = sys.argv[1:4]

with open(vtt_list, 'r') as f:
    for line in f:
        count = ''
        vtt_path = line.strip()
        utt = os.path.basename(vtt_path).replace('.%s.vtt' % lang, '')
        txt = vtt2txt(open(vtt_path, "r").readlines())
        for t in txt:
            each_info = f"{t[0]:1.3f}\t{t[1]:1.3f}\t{t[2]}"
            count += str(each_info) + '\n'
        with open('%s/%s.txt' % (save_path, utt), 'w') as ff:
            ff.write(count)
