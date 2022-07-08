from tqdm import tqdm

def get_error_file(in_file,in_file_refer,out_file):
    with open(in_file,"r") as f_in, open(in_file_refer, "r") as f_in_refer:
        lines = f_in.readlines()
        lines_refer = f_in_refer.readlines()

    new_lines = []
    for i in tqdm(range(len(lines))):
        line = lines[i]

        if line.startswith("WER:") and not line.startswith("WER: 0.00 %"):
            new_lines.append(lines[i-1])
            new_lines.append(line)
            new_lines.append(lines[i+1])
            new_lines.append(lines[i+2])
            if lines[i+2] != lines_refer[i+2]:
                new_lines.append(lines_refer[i+1])
            new_lines.append("\n")
    
    with open(out_file,"w") as f_w:
        f_w.writelines(new_lines)

if __name__=="__main__":
    get_error_file("/work/yangmeng03/wenet/examples/wenetspeech/s0/onnx/u2++_finetune_v20220526/chunk_16_leftChunk_-1/result/lm_runtime/wer",
    "/work/yangmeng03/wenet/examples/wenetspeech/s0/onnx/u2++_finetune_v20220526/chunk_16_leftChunk_-1/result/withoutlm_runtime/wer",
    "/work/yangmeng03/wenet/examples/wenetspeech/s0/onnx/u2++_finetune_v20220526/chunk_16_leftChunk_-1/result/lm_runtime/error_analysis")