import sys, os
import re

def has_digit(string):
    return bool(re.search(r'\d', string))

pattern = re.compile(r"[a-zA-Zàâçéèêëîïôûùüÿñæœ\s'-]")

with open(sys.argv[1], 'r') as f:
    for line in f:
        utt, ref = line.strip().split(' ', 1)
        if has_digit(ref) or ' -' in ref or '- ' in ref or '/' in ref or '%' in ref:
            pass
        else:
            char_to_save = re.findall(pattern, ref.lower())
            each_ref = ''.join([char if char in char_to_save else ' ' for char in ref.lower()])
            each_ref = re.sub(' +', ' ', each_ref.strip())
            print(utt, each_ref.strip())

            
