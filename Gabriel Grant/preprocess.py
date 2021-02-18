import re
import nltk
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet as wn
en_stop = set(nltk.corpus.stopwords.words('english'))


def regex(text):
    text = re.sub(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"," ",text)
    text = re.sub(r"[0-9]{2}\:[0-9]{2}\:[0-9]{2}"," ",text)
    text = re.sub(r'\d+'," ",text)
    text = re.sub(r"[^A-Za-z0-9 ]+"," ",text)
    text = re.sub(r"XXXXX"," ",text)
    text = re.sub(r"sshd"," ",text)
    return text

def tokenizer(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token for token in tokens if len(token) > 3]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens

def preprocess(text):
    complete = tokenizer(regex(text))
    return complete

def full_preprocess(data_text):
    return data_text['log'].map(preprocess)