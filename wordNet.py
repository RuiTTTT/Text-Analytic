import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def is_adj(tag):
    return tag in ['JJ', 'JJR', 'JJS']

def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']

def is_adv(tag):
    return tag in ['RB', 'RBR', 'RBS']

def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

def treeBank_to_wordNet(tag):
    if is_adj(tag):
        return 'a'
    elif is_noun(tag):
        return 'n'
    elif is_adv(tag):
        return 'r'
    elif is_verb(tag):
        return 'v'
    return None

f = open('C:/Users/ray/Documents/UCD/Text Analytics/raw2.txt')
text = f.read()
tokens = [word.lower() for word in word_tokenize(text)]
pos = nltk.pos_tag(tokens)
wnl = []

for word, tag in pos:
    tag = treeBank_to_wordNet(tag)
    if tag is None:
        wnl.append(WordNetLemmatizer().lemmatize(word))
    else:
        wnl.append(WordNetLemmatizer().lemmatize(word, tag))
print(wnl)
