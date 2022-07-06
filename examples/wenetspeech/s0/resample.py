import os
import librosa
import soundfile as sf
from tqdm import tqdm

scp_path = '/work/yangmeng03/wenet/examples/wenetspeech/s0/data/test'
out_dir = '/work/yangmeng03/wenet/examples/wenetspeech/s0/data/audio_re'

resample = 16000

wav_scp = os.path.join(scp_path, 'wav_new.scp')
f1 = open(wav_scp, 'r')

wav_scp_re = os.path.join(scp_path, 'wav_new.scp_re')
f2 = open(wav_scp_re, 'w')

lines = f1.readlines()
for line in tqdm(lines):

    line = line.strip()
    split = line.split()
    wav_name = split[0]
    wav_path = split[1]
    wav_suf = wav_path.split('/')[-1]

    audio, fs = sf.read(wav_path)

    if fs != resample:
        audio_re = librosa.resample(audio, orig_sr=fs, target_sr=resample)
    else:
        audio_re = audio

    out_path = os.path.join(out_dir, wav_suf)
    sf.write(out_path, audio_re, resample)

    f2.write(wav_name + ' ' + out_path + '\n')

f1.close()
f2.close()