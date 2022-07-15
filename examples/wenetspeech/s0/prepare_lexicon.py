lexicon_set = set()
with open("data/lexicon.txt", "r") as f_in:
    lines = f_in.readlines()
    for line in lines:
        items = line.split(" ")
        if len(items)==0:
            continue
        lexicon_set.add(items[0].strip()+"\n")

with open("data/local/lm/text", "r") as f_in, \
    open("data/lexicon_new.txt", 'w') as f_out:
    lines = f_in.readlines()
    for line in lines:
        items = line.split(" ")
        if len(items)<=1:
            continue
        for i in range(1, len(items)):
            word = items[i]
            if word.strip()!="":
                lexicon_set.add(word.strip()+"\n")
    
    f_out.writelines(list(lexicon_set))
    
