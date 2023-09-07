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

train_file = open(train_file_name, 'w', encoding='utf-8')
train_file.write(train_split)
train_file.close()

print("Train file has been written successfully")

val_file = open(val_file_name, 'w', encoding='utf-8')
val_file.write(val_split)
val_file.close()

print("Validation file has been written successfully")

vocab_file = open(vocab_file_name, 'w', encoding='utf-8')
vocab_file.write(vocab)
vocab_file.close()

print("Vocabulary window is made successfully.")

print(f"All: {len(input_content)}, Train: {len(train_split)}, Val: {len(val_split)}, Vocab Size: {len(vocab)}")
