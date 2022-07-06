#!/usr/bin/env bash
# Copyright 2021 Mobvoi Inc. All Rights Reserved.
# Author: binbinzhang@mobvoi.com (Binbin Zhang)
export GLOG_logtostderr=1
export GLOG_v=2

set -e

nj=1

# For CTC WFST based decoding
fst_root=/home/wenet2/examples/wenetspeech/s0/data/lang_test
fst_path=$fst_root/TLG.fst
dict_file=$fst_root/words.txt
acoustic_scale=10.0
beam=15.0
lattice_beam=7.5
min_active=200
max_active=7000
blank_skip_thresh=0.98

# data path
scp=/home/wenet2/examples/wenetspeech/s0/data/test/wav_new.scp_re
label_file=/home/wenet2/examples/wenetspeech/s0/data/test/text

# decode params
chunk_size=16
num_left_chunks=-1
sample_rate=16000
num_bins=80
num_threads=1
ctc_weight=0.3
reverse_weight=0.3
rescoring_weight=1.0

# model path
onnx_model_root=/home/wenet2/examples/wenetspeech/s0/onnx/u2++_finetune_v20220526
onnx_model_dir=$onnx_model_root/chunk_${chunk_size}_leftChunk_${num_left_chunks}
result_dir=$onnx_model_dir/result
dir=$result_dir/lm_runtime

mkdir -p $dir/split${nj}

# Step 1. Split wav.scp
split_scps=""
for n in $(seq ${nj}); do
  split_scps="${split_scps} ${dir}/split${nj}/wav.${n}.scp"
done
tools/data/split_scp.pl ${scp} ${split_scps}

# Step 2. Parallel decoding
wfst_decode_opts=
if [ ! -z $fst_path ]; then
  wfst_decode_opts="--fst_path $fst_path"
  wfst_decode_opts="$wfst_decode_opts --beam $beam"
  wfst_decode_opts="$wfst_decode_opts --lattice_beam $lattice_beam"
  wfst_decode_opts="$wfst_decode_opts --max_active $max_active"
  wfst_decode_opts="$wfst_decode_opts --min_active $min_active"
  wfst_decode_opts="$wfst_decode_opts --acoustic_scale $acoustic_scale"
  wfst_decode_opts="$wfst_decode_opts --blank_skip_thresh $blank_skip_thresh"
  echo $wfst_decode_opts > $dir/config
fi
for n in $(seq ${nj}); do
{
  ./build/decoder_main \
     --rescoring_weight $rescoring_weight \
     --ctc_weight $ctc_weight \
     --reverse_weight $reverse_weight \
     --chunk_size $chunk_size \
     --sample_rate $sample_rate \
     --num_bins $num_bins \
     --wav_scp ${dir}/split${nj}/wav.${n}.scp \
     --onnx_dir $onnx_model_dir \
     --dict_path $dict_file \
     $wfst_decode_opts \
     --result ${dir}/split${nj}/${n}.text &> ${dir}/split${nj}/${n}.log
} &
done
wait

# Step 3. Merge files
for n in $(seq ${nj}); do
  cat ${dir}/split${nj}/${n}.text
done > ${dir}/text
tail $dir/split${nj}/*.log | grep RTF | awk '{sum+=$NF}END{print sum/NR}' > $dir/rtf

# Step 4. Compute WER
python3 tools/compute-wer.py --char=1 --v=1 \
  $label_file $dir/text > $dir/wer
