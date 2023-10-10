import sys, os

used_list, all_list = sys.argv[1:3]

utt_dict = {}
with open(used_list, 'r') as f:
    for line in f:
        utt = line.strip()
        utt_dict[utt] = 1

with open(all_list, 'r') as f:
    for line in f:
        utt = line.strip().split(',')[0]
        if utt not in utt_dict:
            print(line.strip())
