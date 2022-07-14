. ./path_kaldi.sh || exit 1;

lm="data/local/lm"
mkdir -p $lm
<<comment
tools/filter_scp.pl \
	data/train/text \
	data/data_aishell/transcript/aishell_transcript_v0.8.txt > $lm/text
comment
cp data/text_seg $lm/text
local/aishell_train_lms.sh
