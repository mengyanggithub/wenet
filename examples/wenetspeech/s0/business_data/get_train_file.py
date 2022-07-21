from tqdm import tqdm
import jieba

def seg_len(in_str,out_str):
    out_items = jieba.cut(in_str)
    out_str = " ".join(out_items)

    return out_str

def filter_punc(in_list):
    punc_list = ["!","\"","#","$","%","&","'","(",")","*","+",","," ","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~","。","，","？","！","，"," ","（","：","）"]
    filter(lambda in_list:in_list in punc_list, in_list)
    out_list = [item for item in in_list if item not in punc_list]
    return out_list

def process(in_file_name, out_file_name):
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

    with open(out_file_name, "w") as f_out:
        f_out.writelines(new_lines)

if __name__=="__main__":
    process("/work/yangmeng03/data/asr/qiyu/2022-07-20/000000_0_content","/work/yangmeng03/data/asr/qiyu/2022-07-20/train.txt")



