import os

input_file_name = 'minifreud.txt'
vocab_file_name = 'vocab.txt'
train_file_name = 'train.txt'
val_file_name = 'val.txt'

input_file = open(input_file_name, encoding='utf-8')
input_content = input_file.read()

vocab = set(input_content)
