# Import libraries and data
"""

import re
import torch
from torch.utils.data import TensorDataset
from collections import Counter

def read_file(filepath):
  with open(filepath) as f:
        str_text = clean(f.read())
  return str_text

"""# Cleans up text

"""

def clean(input):
  text = input.lower()
  text = re.sub('\n\n \n\n\n!"-#$%&()--.*+,-/:;<=>?@[\\]^_`{|}~\t\n ', text)    
  return text

"""# Assigns each word an integer id

"""

def get_vocab(corpus, min_occurences):
    vocab = Counter()
    for word in corpus:
        vocab[word] += 1

    vocab_top = Counter({k: c for k, c in vocab.items() if c >= min_occurences})
    vocab_tuples = vocab_top.most_common(len(vocab_top))

    word_to_id = Counter({word: i+1 for i,(word, c) in enumerate(vocab_tuples)})
    id_to_word = ["_"] + [word for word, index in word_to_id.items()]

    return word_to_id, id_to_word

"""# coverts the tokenized text to training data: label is a word in the text, and feature is the n preceding words"""

def get_tensor_dataset(list_of_ids, n):
    features = []
    labels = []
    for i in range(n, len(list_of_ids)):
        labels.append(list_of_ids[i])
        features.append(list_of_ids[i-n:i])

    return TensorDataset(torch.tensor(features), torch.tensor(labels))