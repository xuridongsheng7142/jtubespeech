import sys, os

sub_csv, videoid_txt = sys.argv[1:3]

with open(sub_csv, 'r') as f:
    lines = f.readlines()

id_dict = {}
for i in range(1, len(lines)):
    line = lines[i]
    id = line.strip().split(',')[0]
    id_dict[id] = 1

with open(videoid_txt, 'r') as f:
    for line in f:
        id = line.strip()
        if id not in id_dict:
            print(id)
