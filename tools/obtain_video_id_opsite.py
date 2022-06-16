import time
import requests
import argparse
import re
import sys, os
sys.path.append('scripts')
from pathlib import Path
from util import make_query_url
from tqdm import tqdm
import multiprocessing
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

def get_one_id(word):
   
    logging.info('process word {}'.format(word))
    url = make_query_url(word)
    html = requests.get(url).content
  
    videoids_found = [x.split(":")[1].strip("\"").strip(" ") for x in re.findall(r"\"videoId\":\"[\w\_\-]+?\"", str(html))]
    videoids_found = list(set(videoids_found))
    
    count = ''
    for v in videoids_found:
        count += v + '\n'
    return count
  
def pasrse_page(x):
    if x != None and x != "\n":
        with open(fn_videoid,'a') as f:
            f.write(x)

if __name__ == "__main__":

    fn_word, fn_videoid = sys.argv[1:3]

    if not os.path.exists(os.path.dirname(fn_videoid)): os.makedirs(os.path.dirname(fn_videoid))
    if os.path.exists(fn_videoid): os.remove(fn_videoid)

    with open(fn_word, 'r') as f:
        lines = f.readlines()

    for line in reversed(lines):
        result = get_one_id(line.strip())
        pasrse_page(result)

