import os
import json
from tqdm import tqdm
import jieba
import re

import argparse

class data_processor():
    def __init__(self, raw_data_path, train_path):
        self.raw_data_path = raw_data_path
        self.train_path = train_path

    def get_train_text_file(self):
        pass
    def get_lexicon_file(self):
        lexicon_set = set()
        with open("./lexicon.txt", "r") as f_in:
            lines = f_in.readlines()
            for line in lines:
                items = line.split(" ")
                if len(items)==0:
                    continue
                lexicon_set.add(items[0].strip()+"\n")

        if not os.path.exists(self.train_path):
            os.makedirs(self.train_path)

        train_text_file = os.path.join(self.train_path,"text")
        lexicon_file = os.path.join(self.train_path,"lexicon.txt")

        with open(train_text_file, "r") as f_in:
            lines = f_in.readlines()
            for line in tqdm(lines):
                items = line.split(" ")
                if len(items)<1:
                    continue
                lexicon_set.update([word.strip()+"\n" for word in items])

        with open(lexicon_file, "w") as f_out:
            f_out.writelines(lexicon_set)

    def remove_useless_char_and_extra_space(self,a_str):
        useless_char="!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~（）。，！《》「」、：﹕“”abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        new_str = a_str.translate(str.maketrans('', '', useless_char))
        new_str = re.sub(" +"," ",new_str)
        return new_str

        
        

class wiki_zh_data_processor(data_processor):
    def get_train_text_file(self):

        # get all file path
        sub_dir_list = os.listdir(self.raw_data_path)
        file_path_list = []
        for sub_dir in sub_dir_list:
            file_path = os.path.join(self.raw_data_path,sub_dir)
            file_name_list = os.listdir(file_path)
            file_path_list.extend([os.path.join(file_path,file_name) for file_name in file_name_list])

        line_list = []
        for file in file_path_list:
            with open(file, "r") as f:
                json_list = f.readlines()
                line_list.extend([json.loads(json_str)["text"] for json_str in json_list])

        if not os.path.exists(self.train_path):
            os.makedirs(self.train_path)
        
        train_text_file = os.path.join(self.train_path,"text")
        with open(train_text_file, "w") as f_out:
            for line in tqdm(line_list):
                line = " ".join(jieba.cut(line))
                line = self.remove_useless_char_and_extra_space(line).strip()
                if line!="":
                    f_out.write(line)

    def remove_useless_char_and_extra_space(self,a_str):
        useless_char="!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~（）。，！《》「」、：﹕“”abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        new_str = a_str.translate(str.maketrans('', '', useless_char))
        new_str = re.sub(" +"," ",new_str)
        new_str = re.sub("\n \n ","\n",new_str)
        return new_str    

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='processor for big data')
    parser.add_argument('--data',
                        default="wiki_zh")
    parser.add_argument('--raw_data_path')
    parser.add_argument('--data_path')

    args = parser.parse_args()
    
    if args.data=="wiki_zh":
        processor = wiki_zh_data_processor(args.raw_data_path,args.data_path)
        processor.get_train_text_file()
        processor.get_lexicon_file()

