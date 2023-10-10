import re
import sys

wav_scp = sys.argv[1]

ID_dict = {}
with open(wav_scp, 'r') as f:
    for line in f:
        utt = line.strip().split(' ')[0]
        ID = re.sub(r"_\d+_\d+$", "", utt)
        if ID not in ID_dict:
            ID_dict[ID] = 1
            print(ID)

