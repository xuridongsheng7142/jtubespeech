import sys, os, re

ref_txt, ref_fix = sys.argv[1:3]

def remove_punctuation(text):
    # 删除词尾的标点
    words = text.split()
    clean_words = [word.strip('.,;:!?"').strip() for word in words if word.rstrip('.,;:!?"')]
    clean_text = ' '.join(clean_words)
    return clean_text

with open(ref_txt, 'r') as f, open(ref_fix, 'w') as ff:
    for line in f:
        utt, ref = line.strip().split(' ', 1)
        ref = remove_punctuation(ref)
        ref = ref.upper()
        if '-' in ref or '(' in ref or ')' in ref:
            pass
        else:
            print(utt, ref, file=ff)
