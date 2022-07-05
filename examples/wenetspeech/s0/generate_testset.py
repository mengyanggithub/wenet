from tqdm import tqdm
import string

with open("./data/test/wav.scp", "r") as f_in:
    lines = f_in.readlines()

new_lines = []
for line in tqdm(lines):
    new_line = line.replace("/work/zhangjincheng01/asr/data/test/test_v20220321/","/work/yangmeng03/wenet/examples/wenetspeech/s0/data/test/")
    new_lines.append(new_line)

with open("./data/test/wav_new.scp", "w") as f_out:
    f_out.writelines(new_lines)
