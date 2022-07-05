from tqdm import tqdm
import jieba


def seg_file(in_file_name,out_file_name):
    with open(in_file_name,"r") as f_in:
        lines = f_in.readlines()
    
    new_lines = []
    for line in tqdm(lines):
        items = line.split(" ")
        if len(items)==2:
            seg_item = jieba.cut(items[1])
            new_line = items[0]+" "+" ".join(seg_item)
            new_lines.append(new_line)

    with open(out_file_name, "w") as f_out:
        f_out.writelines(new_lines)

if __name__=="__main__":
    seg_file("./data/text","./data/text_seg")