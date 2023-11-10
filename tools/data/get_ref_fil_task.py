import sys, os
import re
import json

text, lang = sys.argv[1:3]

def has_digit(string):
    return bool(re.search(r'\d', string))

re_dict = {}
with open('conf/re.txt', 'r') as f:
    for line in f:
        task, match_info = line.strip().split('\t')
        re_dict[task] = match_info

with open('conf/replace.json', 'r') as f:
    json_str = json.load(f)

replace_dict = {}
if lang in json_str:
    replace_dict = json_str[lang]

if lang not in re_dict:
    print('lang not in re_dict !!!')
    exit (1)

match_info = re_dict[lang]
pattern = re.compile(match_info)

with open(text, 'r') as f:
    for line in f:
        utt, ref = line.strip().split(' ', 1)
        if has_digit(ref) or ' -' in ref or '- ' in ref or '/' in ref or '%' in ref:
            pass
        else:
            for key, value in replace_dict.items():
                ref = ref.replace(key, value)
            char_to_save = re.findall(pattern, ref.lower())
            each_ref = ''.join([char if char in char_to_save else ' ' for char in ref.lower()])
            each_ref = re.sub(' +', ' ', each_ref.strip())
            print(utt, each_ref.strip())

            
