#!/usr/bin/env python

import sys

def replace_x01_with_pipe(input_lines):
    output_lines = []
    for line in input_lines:
        output_lines.append(line.replace('\x01', '|'))
    return output_lines

def main():
    # 从标准输入中读取输入
    input_lines = sys.stdin.readlines()

    # 替换 'x01' 为 '|'
    output_lines = replace_x01_with_pipe(input_lines)

    # 将结果输出到标准输出
    for line in output_lines:
        sys.stdout.write(line)

if __name__ == "__main__":
    main()
