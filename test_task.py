import sys
import re

def load_config(file_name):
    replace_pairs = {}
    with open(file_name, 'r') as file:
        for line in file:
            if line.strip():
                value1, value2 = line.strip().split('=')
                replace_pairs[value1] = value2
    return replace_pairs

def replace_text(file_name, replace_pairs):
    lines = []
    with open(file_name, 'r') as file:
        for line in file:
            original_line = line.strip()
            replaced_line = original_line
            replaced_count = 0
            for value1, value2 in replace_pairs.items():
                replaced_line, count = re.subn(rf'{value1}', value2, replaced_line)
                replaced_count += count
            lines.append((replaced_line, replaced_count, original_line))
    return lines

def main(config_file, text_file):
    replace_pairs = load_config(config_file)
    replaced_lines = replace_text(text_file, replace_pairs)
    sorted_lines = sorted(replaced_lines, key=lambda x: x[1], reverse=True)
    for line, count, original in sorted_lines:
        print(f'Original: {original}')
        print(f'Replaced: {line}')
        print(f'Symbols replaced: {count}\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <config_file> <text_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    text_file = sys.argv[2]
    
    main(config_file, text_file)
