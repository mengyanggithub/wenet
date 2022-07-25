from tqdm import tqdm

def get_error_file(in_file,in_file_refer,out_file, out_file_2):
    with open(in_file,"r") as f_in, open(in_file_refer, "r") as f_in_refer:
        lines = f_in.readlines()
        lines_refer = f_in_refer.readlines()

    new_lines = []
    new_lines_2 = []
    for i in tqdm(range(len(lines))):
        line = lines[i]

        if line.startswith("WER:") and not line.startswith("WER: 0.00 %"):
            if lines[i+2] != lines_refer[i+2]:
                new_lines_2.append(lines[i-1])
                new_lines_2.append(line)
                new_lines_2.append(lines[i+1])
                new_lines_2.append(lines[i+2])
                new_lines_2.append(lines_refer[i+2])
                new_lines_2.append("\n")
            else:
                new_lines.append(lines[i-1])
                new_lines.append(line)
                new_lines.append(lines[i+1])
                new_lines.append(lines[i+2])
                new_lines.append("\n")
    
    with open(out_file,"w") as f_w:
        f_w.writelines(new_lines)
    with open(out_file_2,"w") as f_w_2:
        f_w_2.writelines(new_lines_2)

def get_diff_file(in_file,in_file_refer,out_file):
    with open(in_file,"r") as f_in, open(in_file_refer, "r") as f_in_refer:
        lines = f_in.readlines()
        lines_refer = f_in_refer.readlines()

    new_lines = []
    for i in tqdm(range(len(lines))):
        line = lines[i]

        if line.startswith("rec:") and line != lines_refer[i]:
            new_lines.append(lines[i-3])
            new_lines.append(lines[i-1])
            new_lines.append(lines_refer[i])
            new_lines.append(lines[i])
    
    with open(out_file, "w") as f_w:
        f_w.writelines(new_lines)

if __name__=="__main__":
    '''
    get_error_file("/work/yangmeng03/wenet/examples/wenetspeech/s0/onnx/u2++_finetune_v20220526/chunk_16_leftChunk_-1/result/lm_runtime/wer",
    "/work/yangmeng03/wenet/examples/wenetspeech/s0/onnx/u2++_finetune_v20220526/chunk_16_leftChunk_-1/result/withoutlm_runtime/wer",
    "/work/yangmeng03/wenet/examples/wenetspeech/s0/onnx/u2++_finetune_v20220526/chunk_16_leftChunk_-1/result/lm_runtime/error_analysis",
    "/work/yangmeng03/wenet/examples/wenetspeech/s0/onnx/u2++_finetune_v20220526/chunk_16_leftChunk_-1/result/lm_runtime/error_analysis_2")
    '''
    '''
    get_diff_file(
        "/work/yangmeng03/wenet/examples/wenetspeech/s0/all_data/no_lm/wer",
        "/work/yangmeng03/wenet/examples/wenetspeech/s0/all_data/real_train_v1/wer",
        "/work/yangmeng03/wenet/examples/wenetspeech/s0/diff_analysis_nolm_realtrain.txt"
    )
    '''
    get_diff_file(
        "/work/yangmeng03/wenet/examples/wenetspeech/s0/all_data/real_train_v1/wer",
        "/work/yangmeng03/wenet/examples/wenetspeech/s0/all_data/qiyu_20220719_3gram/lm_runtime_2022_07_19/wer",
        "/work/yangmeng03/wenet/examples/wenetspeech/s0/diff_analysis_realtrain_qiyu_20220719_3gram.txt"
    )
