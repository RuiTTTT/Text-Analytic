import math
import string
from textblob import TextBlob
from nltk.corpus import stopwords


def remove_punc(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return ''.join([char for char in text if not char.isdigit()])


def remove_stopwords(text):
    return set(text.words) - set(english_stopwords)


def tf(word, blob):
    return blob.words.count(word) / len(remove_stopwords(blob))


def n_occurance(word, bloblist):
    return sum(1 for blob in bloblist if word in remove_stopwords(blob))


def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_occurance(word, bloblist)))


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


english_stopwords = stopwords.words('english')

d1 = TextBlob(remove_punc(
    "Most places dry overnight, some mist or fog patches. Some rain or drizzle mainly near North & SouthWest coasts.  Lows 7 to 10 C, in light westerlies."))
d2 = TextBlob(remove_punc(
    "Cloudy & misty tonight.Dry weather, but rain / drizzle at times, mainly near SouthWest & North coasts. Lows 7/10 C.,in light West or variable breezes."))
d3 = TextBlob(remove_punc(
    "Dry in many areas this afternoon & evening,but mostly cloudy, outbreaks of rain & drizzle. A few bright spells in places also. Highs 13/16 C"))
d4 = TextBlob(remove_punc(
    "Rather cloudy this aft. Dry in many places but there will be some sctd outbreaks of rain, & possibly  more persistent rain in parts of the North"))
d5 = TextBlob(remove_punc(
    "Rather cloudy, some sunny breaks developing in places. Dry in many areas, but there will be some shwry outbreaks of rain, mainly in North & NorthWest"))
d6 = TextBlob(remove_punc(
    "Mostly cloudy today. Some hazy sunnyspells. Mainly dry. Patchy light rain in far SouthWest this morn & isol patches of drzl near NorthWest coasts.High 13-16 C"))
d7 = TextBlob(remove_punc(
    "Mild & breezy overnight.Scattered patches of rain & drzl at times - mainly over Muns, but many areas will stay dry. Lows 9 to 12 degrees."))
d8 = TextBlob(remove_punc(
    "Breezy, misty & mostly cloudy this evening & tonight, with patches of rain & drizzle at times. Mild, lowest temperatures 9 to 12 C."))
d9 = TextBlob(remove_punc(
    "Dry in many areas this aft. but mostly cloudy. However patchy rain, drizzle and mist along Atlantic coastal counties will slowly extend East."))
d10 = TextBlob(remove_punc(
    "Dry in many areas this aft, with a few bright spells, but predominantly cloudy, with a little patchy rain or drizzle in places. 12/15 C."))

bloblist = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]

word_set = []
pmi = {}
for blob in bloblist:
    word_set = word_set + list(remove_stopwords(blob))
word_set = set(word_set)
for worda in word_set:
    for wordb in word_set:
        count = 0
        for blob in bloblist:
            if worda != wordb:
                if worda in remove_stopwords(blob) and wordb in remove_stopwords(blob):
                    count = count + 1
        # print(worda, wordb, count)
        pmi[worda + ' ' + wordb] = count
print(sorted(pmi.items(), key=lambda x: x[1], reverse=True))
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

# print(remove_stopwords(d1))
