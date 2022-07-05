. ./path.sh || exit 1;

dir=./
./tools/decode.sh --nj 16 \
	--beam 15.0 --lattice_beam 7.5 --max_active 7000 \
	--blank_skip_thresh 0.98 --ctc_weight 0.5 --rescoring_weight 1.0 \
	--fst_path data/lang_test/TLG.fst \
	data/test/wav.scp data/test/text $dir/final.zip \
	data/lang_test/words.txt $dir/lm_with_runtime
