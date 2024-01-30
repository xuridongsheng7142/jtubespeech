import sys, os

text1, text2 = sys.argv[1:3]

ref_dict = {}
with open(text1, 'r') as f:
    for line in f:
        utt, ref = line.strip().split(' ', 1)
        ref_dict[utt] = ref

with open(text2, 'r') as f:
    for line in f:
        utt, ref = line.strip().split(' ', 1)
        if utt in ref_dict:
            if ref.lower() != ref_dict[utt].lower():
                print(utt + '\t' +  ref_dict[utt] + '\t' + ref)
