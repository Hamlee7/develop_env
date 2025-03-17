#!/bin/bash

# 输入和输出目录
# input_dir="8k"
# output_dir="16k"
input_dir=$1
output_dir=$2

# 确保输出目录存在
mkdir -p "$output_dir"

# 遍历输入目录中的所有 .wav 文件
for input_file in "$input_dir"/*.wav; do
    # 获取文件名（不包含路径）
    filename=$(basename "$input_file")

    # 构造输出文件路径
    output_file="$output_dir/$filename"

    # 使用 ffmpeg 进行音频采样率转换
    ffmpeg -i "$input_file" -ar 16000 "$output_file"

    echo "Processed $input_file -> $output_file"
done

echo "Batch processing complete."
