#!/bin/bash  

: ' 
python ./data_processor.py \
    --data wiki_zh \
    --raw_data_path /work/yangmeng03/data/wiki_zh\
    --data_path /work/yangmeng03/wenet/examples/wenetspeech/s0/big_data/train_wiki_zh
'

: '
python ./data_processor.py \
    --data qiyu \
    --raw_data_path /work/yangmeng03/data/qiyu\
    --raw_data_file all_qiyu_20220729 \
    --data_path /work/yangmeng03/wenet/examples/wenetspeech/s0/big_data/train_qiyu
'

python ./data_processor.py \
    --data qiyu \
    --data_path /work/yangmeng03/wenet/examples/wenetspeech/s0/big_data/train_qiyu \
    --ratio 10

