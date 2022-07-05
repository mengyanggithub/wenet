. ./path.sh || exit 1;

python wenet/bin/export_jit.py \
--config exp/conformer/train.yaml \
--checkpoint exp/conformer/70.pt \
--output_file final.zip \
--output_quant_file final_quant.zip
