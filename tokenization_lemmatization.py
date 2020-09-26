from collections import defaultdict
from nltk.corpus import wordnet
from nltk.tokenize import TreebankWordTokenizer
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
import pandas as pd

stopwords_list = pd.read_pickle('stopwords_list.pkl')
zucchini_list = ['zookeenee','zuc', 'zucc', 'zucch','zucchiini', 'zucchine',\
        'zucchini', 'zucchinies', 'zucchinni','zucchni','zucchnini', 'zucchs',\
        'zuccihini', 'zuccini', 'zuccinni', 'zuccs', 'zuccuni', 'zuch', 'zuchhini',\
        'zuchiini', 'zuchini', 'zuchinies', 'zuchinni', 'zuchinnis', 'zuchs',\
        'zucke', 'zucs', 'zuke','zukes']

def tokenize_lemmatize(text):

    tokens = pos_tag(TreebankWordTokenizer().tokenize(text))

    tag_map = defaultdict(lambda : wordnet.NOUN)
    tag_map['J'] = wordnet.ADJ
    tag_map['V'] = wordnet.VERB
    tag_map['R'] = wordnet.ADV

    lemmatizer = WordNetLemmatizer()

    lemma_holder = []

    for token, tag in tokens:
        
        if token in zucchini_list: # people just cannot spell zucchini I guess
            token = 'zucchini'

        if token in stopwords_list:
            continue
        else:
            lemma = lemmatizer.lemmatize(token, tag_map[tag[0]])
            lemma_holder.append(lemma)

    return ' '.join(lemma_holder)
