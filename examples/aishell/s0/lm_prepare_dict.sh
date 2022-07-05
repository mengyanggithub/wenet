. ./path.sh || exit 1;

dict="data/dict/lang_char.txt"
data="data"

unit_file=$dict
mkdir -p data/local/dict
cp $unit_file data/local/dict/units.txt
tools/fst/prepare_dict.py \
	$unit_file \
	${data}/resource_aishell/lexicon.txt \
	data/local/dict/lexicon.txt
