import os

input_file_name = 'minifreud.txt'
vocab_file_name = 'vocab.txt'
train_file_name = 'train.txt'
val_file_name = 'val.txt'

input_file = open(input_file_name, encoding='utf-8')
input_content = input_file.read()

split_index = int(0.9 * len(input_content))

vocab = set(input_content)
train_split = input_content[:split_index]
val_split = input_content[split_index:]

print(f"All: {len(input_content)}, Train: {len(train_split)}, Val: {len(val_split)}, Vocab Size: {len(vocab)}")
