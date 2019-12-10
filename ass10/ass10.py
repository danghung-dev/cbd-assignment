import spacy
import nltk
from nltk.corpus import gutenberg
nlp = spacy.load('en')
import random
import pandas as pd
import matplotlib.pyplot as plt
# import nltk
# nltk.download('gutenberg')

emma = gutenberg.raw('austen-emma.txt')
parsed_emma = nlp(emma)
print(len(parsed_emma))
print((parsed_emma.sents))
# import re
# sample_size = 100
# my_sample = random.sample(list(parsed_emma.sents),sample_size) # select a random sample of sentences
# sample=[]
# for sent in my_sample:
#     sent = re.sub("\s+"," ",sent.text) # clean up the whitespace
#     print(sent,"\n")
#     sample.append(sent)

# Reference
# https://dzone.com/articles/tensorflow-kaggle-spooky-authors-bag-of-words-mode