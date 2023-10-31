import sys, os, re
sys.path.append('./')
from scripts.util import make_video_url, make_basename, vtt2txt, autovtt2txt, count_total_second
from datetime import datetime as dt
import scipy.io.wavfile as wav_func

wavlist, vtt_list, save_path, lang = sys.argv[1:5]

utt_dict = {}
with open(wavlist, 'r') as f:
    for line in f:
        wav_path = line.strip()
        utt = os.path.basename(wav_path).replace('.wav', '')
        fs, data = wav_func.read(wav_path)
        utt_dict[utt] = data

with open(vtt_list, 'r') as f:
    for line in f:
        count = ''
        vtt_path = line.strip()
        utt = os.path.basename(vtt_path).replace('.%s.vtt' % lang, '')
        with open(vtt_path, "r") as ff:
            for each_line in ff:
                m = re.match(r'(\d+\:\d+\:\d+\.\d+) --> (\d+\:\d+\:\d+\.\d+)', each_line.strip())
                if m is not None:
                    start_time = m.groups()[0]
                    end_time = m.groups()[1]
                    utt_fix = '%s_%s_%s' % (utt, str(start_time), str(end_time))
                    st = count_total_second(dt.strptime(m.groups()[0], "%H:%M:%S.%f"))
                    et = count_total_second(dt.strptime(m.groups()[1], "%H:%M:%S.%f"))
                    start_point = int(float(st) * 16000)
                    end_point = int(float(et) * 16000)
                    if utt in utt_dict: 
                        each_data = utt_dict[utt][start_point:end_point]
                        save_data = '%s/%s.wav' % (save_path, utt_fix)
                        wav_func.write(save_data, 16000, each_data)
                
