from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords, brown
from nltk import FreqDist
import pickle

def preprocess(sentence_list,label):
    document = []
    for sentence in sentence_list:
        filtered_words = tokenize(sentence)
        labeled = (filtered_words,label)
        document.append(labeled)
    return document


def tokenize(sentence):
    sentence = sentence.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(sentence)
    filtered_words = [w for w in tokens if not w in stopwords.words('english')]
    return filtered_words


def get_feature(token_list,frequency_list):
    wordlist = frequency_list[:5000]
    features = {}
    for w in wordlist:
        features[w[0]] = w[0] in token_list
    return features

#print(get_feature(["above", "love", "you", "and", "her", "and", "everyone"]))
'''
set = stopwords.words('english')
frequency_list = FreqDist(i.lower() for i in brown.words() if i.isalpha() and i not in set and i.lower() not in set)
wordlist = frequency_list.most_common()[:5000]
with open("C:/Users/Kang/trunk/pickle/allWords.pickle","wb") as f:
    pickle.dump(wordlist,f,protocol=2)
'''