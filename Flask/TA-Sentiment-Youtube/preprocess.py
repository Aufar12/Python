import pandas as pd
from mtranslate import translate
import string
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def english_translate(arrayComments):
    translated = []
    for i in arrayComments:
        translations = translate(i, 'en')
        translated.append(translations)

    return translated

def lowercase(arrayComments):
    lower = arrayComments
    lower = [x.lower() for x in lower]
    return lower

def remove_punctuation(text):
    """custom function to remove the punctuation"""
    PUNCT_TO_REMOVE = string.punctuation
    return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))

def remove_stopwords(text):
    STOPWORDS = set(stopwords.words('english'))
    """custom function to remove the stopwords"""
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])


def remove_freqwords(arrayComments):
    """custom function to remove the frequent words"""
    cnt = Counter()
    for text in arrayComments:
        for word in text.split():
            cnt[word] += 1

    cnt.most_common(10)
    FREQWORDS = set([w for (w, wc) in cnt.most_common(5)])

    def remove_freq(text):
        """custom function to remove the frequent words"""
        return " ".join([word for word in str(text).split() if word not in FREQWORDS])

    array = arrayComments.apply(lambda text: remove_freq(text))
    return array


def remove_rarewords(arrayComments):
    """custom function to remove the rare words"""
    cnt = Counter()
    for text in arrayComments:
        for word in text.split():
            cnt[word] += 1

    cnt.most_common(10)

    n_rare_words = 10
    RAREWORDS = set([w for (w, wc) in cnt.most_common()[:-n_rare_words - 1:-1]])
    def remove_rare(text):
        return " ".join([word for word in str(text).split() if word not in RAREWORDS])

    array = arrayComments.apply(lambda text: remove_rare(text))
    return array

def stem_words(arrayComments):
    stemmer = PorterStemmer()

    def stem(text):
        return " ".join([stemmer.stem(word) for word in text.split()])

    array = arrayComments.apply(lambda text: stem(text))
    return array

def lemmatize_words(arrayComments):
    lemmatizer = WordNetLemmatizer()
    def lemmatize(text):
        return " ".join([lemmatizer.lemmatize(word) for word in text.split()])

    array = arrayComments.apply(lambda text: lemmatize(text))
    return array

def remove_emoticon(arrayComments):
    def deEmojify(text):
        return text.encode('CP855', 'ignore').decode('CP855')

    temp = arrayComments
    emot = []

    for i in temp:
        x = deEmojify(i)
        emot.append(x)

    return emot

def automated_labelling(arrayComments):
    label = []
    analyzer = SentimentIntensityAnalyzer()
    p = 0
    n = 0
    ne = 0

    for sentence in arrayComments:
        vs = analyzer.polarity_scores(sentence)

        if (vs['compound'] > 0):
            temp = "Positive"
            label.append(temp)
            p += 1
        elif (vs['compound'] < 0):
            temp = "Negative"
            label.append(temp)
            n += 1
        else:
            temp = "Positive"
            label.append(temp)
            ne += 1

    print(str(p) + ", " + str(n) + ", " + str(ne))
    return label

def cleanse(arrayComments):

    # translated = english_translate(arrayComments)
    print('translate')
    lower = lowercase(arrayComments)

    df = pd.DataFrame({"Comments": lower})
    print('lower')
    df["Comments"] = df["Comments"].apply(lambda text: remove_punctuation(text))
    print('punct')
    df["Comments"] = df["Comments"].apply(lambda text: remove_stopwords(text))
    print('stopword')
    df["Comments"] = remove_freqwords(df["Comments"])
    print('freqword')
    df["Comments"] = remove_rarewords(df["Comments"])
    print('rareword')
    df["Comments"] = stem_words(df["Comments"])
    print('stemming')
    df["Comments"] = lemmatize_words(df["Comments"])
    print('lemmatize')
    df["Comments"] = remove_emoticon(df["Comments"])
    print('remove emot')
    cleanComment = df["Comments"]
    label = automated_labelling(cleanComment)

    return cleanComment, label
#
# df = pd.read_csv(r'C:\Users\Aufar\Documents\edm\DataReynie.csv')
# del df['Unnamed: 0']
# arrayComments = []
# for i in df["Comments"]:
#     arrayComments.append(i)
#
# print(arrayComments)
# my_i, my_card = cleanse(arrayComments)
# print(my_i)
# print(my_card)