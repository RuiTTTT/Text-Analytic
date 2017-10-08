import math
import string
from textblob import TextBlob


def remove_punc(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def tf(word,blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word,bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word,blob,bloblist):
    return tf(word, blob) * idf(word, bloblist)

d1 = TextBlob(remove_punc("Most places dry overnight, some mist or fog patches. Some rain or drizzle mainly near North & SouthWest coasts.  Lows 7 to 10 C, in light westerlies.").lower())
d2 = TextBlob(remove_punc("Cloudy & misty tonight.Dry weather, but rain / drizzle at times, mainly near SouthWest & North coasts. Lows 7/10 C.,in light West or variable breezes.").lower())
d3 = TextBlob(remove_punc("Dry in many areas this afternoon & evening,but mostly cloudy, outbreaks of rain & drizzle. A few bright spells in places also. Highs 13/16 C").lower())
d4 = TextBlob(remove_punc("Rather cloudy this aft. Dry in many places but there will be some sctd outbreaks of rain, & possibly  more persistent rain in parts of the North").lower())
d5 = TextBlob(remove_punc("Rather cloudy, some sunny breaks developing in places. Dry in many areas, but there will be some shwry outbreaks of rain, mainly in North & NorthWest").lower())
d6 = TextBlob(remove_punc("Mostly cloudy today. Some hazy sunnyspells. Mainly dry. Patchy light rain in far SouthWest this morn & isol patches of drzl near NorthWest coasts.High 13-16 C").lower())
d7 = TextBlob(remove_punc("Mild & breezy overnight.Scattered patches of rain & drzl at times - mainly over Muns, but many areas will stay dry. Lows 9 to 12 degrees.").lower())
d8 = TextBlob(remove_punc("Breezy, misty & mostly cloudy this evening & tonight, with patches of rain & drizzle at times. Mild, lowest temperatures 9 to 12 C.").lower())
d9 = TextBlob(remove_punc("Dry in many areas this aft. but mostly cloudy. However patchy rain, drizzle and mist along Atlantic coastal counties will slowly extend East.").lower())
d10 = TextBlob(remove_punc("Dry in many areas this aft, with a few bright spells, but predominantly cloudy, with a little patchy rain or drizzle in places. 12/15 C.").lower())

bloblist = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]

for i,blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
