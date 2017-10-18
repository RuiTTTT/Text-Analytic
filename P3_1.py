import math
import string
from textblob import TextBlob
from nltk.corpus import stopwords


def remove_punc(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return ''.join([char for char in text if not char.isdigit()])


def remove_stopwords(text):
    return [item for item in text.words if item not in english_stopwords]


def tf(word, blob):
    return blob.words.count(word)


def n_occurance(word, bloblist):
    return sum(1 for blob in bloblist if word in remove_stopwords(blob))


def idf(word, bloblist):
    return math.log10(len(bloblist) / (1 + n_occurance(word, bloblist)))


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


english_stopwords = stopwords.words('english')

d1 = TextBlob(remove_punc(
    "Most places dry overnight, some mist or fog patches. Some rain or drizzle mainly near North & SouthWest coasts.  Lows 7 to 10 C, in light westerlies."))
d2 = TextBlob(remove_punc(
    "Cloudy & misty tonight. Dry weather, but rain / drizzle at times, mainly near SouthWest & North coasts. Lows 7/10 C.,in light West or variable breezes."))
d3 = TextBlob(remove_punc(
    "Dry in many areas this afternoon & evening, but mostly cloudy, outbreaks of rain & drizzle. A few bright spells in places also. Highs 13/16 C"))
d4 = TextBlob(remove_punc(
    "Rather cloudy this afternoon. Dry in many places but there will be some sctd outbreaks of rain, & possibly  more persistent rain in parts of the North"))
d5 = TextBlob(remove_punc(
    "Rather cloudy, some sunny breaks developing in places. Dry in many areas, but there will be some shwry outbreaks of rain, mainly in North & NorthWest"))
d6 = TextBlob(remove_punc(
    "Mostly cloudy today. Some hazy sunnyspells. Mainly dry. Patchy light rain in far SouthWest this morning & isol patches of drzl near NorthWest coasts.High 13-16 C"))
d7 = TextBlob(remove_punc(
    "Mild & breezy overnight. Scattered patches of rain & drzl at times - mainly over Muns, but many areas will stay dry. Lows 9 to 12 degrees."))
d8 = TextBlob(remove_punc(
    "Breezy, misty & mostly cloudy this evening & tonight, with patches of rain & drizzle at times. Mild, lowest temperatures 9 to 12 C."))
d9 = TextBlob(remove_punc(
    "Dry in many areas this afternoon. but mostly cloudy. However patchy rain, drizzle and mist along Atlantic coastal counties will slowly extend East."))
d10 = TextBlob(remove_punc(
    "Dry in many areas this afternoon, with a few bright spells, but predominantly cloudy, with a little patchy rain or drizzle in places. 12/15 C."))

bloblist = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]

word_set_duplicate = []
co = {}
pmi = {}
for blob in bloblist:
    # print(remove_stopwords(blob))
    word_set_duplicate = word_set_duplicate + list(remove_stopwords(blob))

word_set = set(word_set_duplicate)
for worda in word_set:
    if word_set_duplicate.count(worda) <= 1:
        continue
    for wordb in word_set:
        if word_set_duplicate.count(worda) <= 1:
            continue
        count = 0
        for blob in bloblist:
            if worda != wordb:
                if worda in remove_stopwords(blob) and wordb in remove_stopwords(blob):
                    count = count + 1
        if count == 0:
            continue
        co[worda + ' ' + wordb] = count
        pmi[worda + ' ' + wordb] = math.log2(count) + math.log2(len(word_set_duplicate)) - math.log2(
            word_set_duplicate.count(worda)) - math.log2(word_set_duplicate.count(wordb))
print(sorted(pmi.items(), key=lambda x: x[1], reverse=True))

total_tfidf = {}
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores_tf = {word: tf(word, blob) for word in remove_stopwords(blob)}
    sorted_tf = sorted(scores_tf.items(), key=lambda x: x[1], reverse=True)
    scores_idf = {word: idf(word, bloblist) for word in remove_stopwords(blob)}
    sorted_idf = sorted(scores_idf.items(), key=lambda x: x[1], reverse=True)
    scores_tfidf = {word: tfidf(word, blob, bloblist) for word in remove_stopwords(blob)}
    sorted_words = sorted(scores_tfidf.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
    print(sorted_tf)
    print(sorted_idf)

total_tf = {}
total_idf = {}
for word in word_set:
    total_tf[word] = word_set_duplicate.count(word)
    total_idf[word] = idf(word, bloblist)
    total_tfidf[word] = total_tf[word] * total_idf[word]
print(sorted(total_tf.items(), key=lambda x: x[1], reverse=True))
sort_tfidf = sorted(total_tfidf.items(), key=lambda x: x[1], reverse=True)
print(sort_tfidf)
aaa = ''
for item in word_set_duplicate:
    aaa = aaa + ' ' + item
print(total_tfidf.keys())
for i in total_tfidf.values():
    print(i * 10, end=',')
print(total_tfidf.items())
