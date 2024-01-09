# Write a Python function to tokenize a sentence using the NLTK library

import nltk

def tokenize_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    return tokens

input_sentence = "NLTK is super duper cool! Try it out."

tokens = tokenize_sentence(input_sentence)
print(tokens)
