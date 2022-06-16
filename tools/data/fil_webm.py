import sys, os

org_webmlist, new_webmlist = sys.argv[1:3]

id_dict = {}
with open(org_webmlist, 'r') as f:
    for line in f:
        id = os.path.basename(line.strip())
        id_dict[id] = 1

result_dict = {}
with open(new_webmlist, 'r') as f:
    for line in f:
        id = os.path.basename(line.strip())
        if id not in id_dict:
            result_dict[id] = line.strip()

for key in result_dict.keys():
    print(result_dict[key])
