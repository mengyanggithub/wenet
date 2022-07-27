from tqdm import tqdm
import jieba
from os import listdir
from os import path

def seg_len(in_str,out_str):
    out_items = jieba.cut(in_str)
    out_str = " ".join(out_items)

    return out_str

def filter_punc(in_list):
    punc_list = ["!","\"","#","$","%","&","'","(",")","*","+",","," ","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~","。","，","？","！","，"," ","（","：","）"]
    filter(lambda in_list:in_list in punc_list, in_list)
    out_list = [item for item in in_list if item not in punc_list]
    return out_list

def process(in_file_name):
    str_set = set()
    with open(in_file_name, "r") as f_in:
        lines = f_in.readlines()
        for line in tqdm(lines):
            if line.startswith('{'):
                continue
            str_set.add(line.strip())

    new_lines = []
    for line in tqdm(str_set):
        seg_item = jieba.cut(line)
        seg_item = filter_punc(seg_item)
        new_line = " ".join(seg_item)
        new_lines.append(new_line+"\n")
    
    return new_lines

def get_train_file(in_dir,out_file_name):
    file_name = [f for f in listdir(in_dir) if "content" in f]
    
    with open(out_file_name, "w") as f_out:
        for file in file_name:
            in_path = path.join(in_dir, file)
            lines = process(in_path)
            f_out.writelines(lines)

if __name__=="__main__":
    # process("/work/yangmeng03/data/asr/qiyu/2022-07-20/000000_0_content","/work/yangmeng03/data/asr/qiyu/2022-07-20/train.txt")
    # get_train_file("/work/yangmeng03/data/asr/qiyu/2022-07-20","/work/yangmeng03/data/asr/qiyu/2022-07-20/train.txt")

    import re
    text = '你好 😂'
    print(text) # with emoji
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    print(emoji_pattern.sub(r'', text)) # no emoji
    


