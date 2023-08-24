# # https://www.natasshaselvaraj.com/how-to-scrape-twitter/

# import twint
# c = twint.Config()

# c.Search = ['Taylor Swift']       # topic
# c.Limit = 500      # number of Tweets to scrape
# c.Store_csv = True       # store tweets in a csv file
# c.Output = "taylor_swift_tweets.csv"     # path to csv file

# twint.run.Search(c)

# =========================================================================

# from twitterscraper import query_tweets
# import datetime as dt
# import pandas as pd

# #Providing the range of days in which I want the data 
# begin_date=dt.date(2021,11,1)
# end_date=dt.date(2021,12,3)

# #Providing limit to the fetched tweets and also specifying the language of the desired tweets
# limit=1000
# language='english'

# #Extracting tweets for the Keyword “Covid-19”
# tweets=query_tweets('Covid-19',limit=limit,
#     begindate=begin_date,
#     enddate=end_date,lang=language)

# df=pd.DataFrame(t.__dict__ for t in tweets)
# print(df)

# =========================================================================

# from twitter_scraper import get_tweets

# for tweet in get_tweets('twitter', pages=1):
#     print(tweet['text'])

#==============================================================

import snscrape.modules.twitter as sntwitter
import pandas as pd
import string, re, inspect, nltk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import networkx as nx
import collections
import time
from scrapOther import scrapOthers

# Topik
topics = ['#KainJarik', '#KekerasanSeksual', '#Pelecehan']
topics += ['Kekerasan Seksual', 'Gilangbungkus', 'Fetish kain jarik', 'Kasus pelecehan seksual kampus UNAIR', 'Mahasiswa', 'Pelecehan Unair',
'Pelecehan seksual', 'Kain jarik', 'Penyimpangan seksual', 'Kelainan seksual', 'Fetish gilang', 'Kasus gilang', 'Riset gilang', 'Gilang fetish', 'Gilang unair',
'Gilang ditangkap', 'Pelaku fetish kain jarik di tangkap', 'Tersangka fetish kain jarik', 'Hukuman gilang']

# Simbol
PUNCT_TO_REMOVE = string.punctuation

# Stopwords
all_language = stopwords.fileids()
all_stopwords = []

for i in all_language:
    lang_stopword = stopwords.words(i)
    all_stopwords += lang_stopword

all_stopwords.extend(['yg', 'ya', 'gw', 'coba'])

# Set variables for counting words
relevant_words, removed_words, total_words = {}, {}, 0
all_hashtags, freq_hashtags = [], []

def scrapTwitter(topics):
    tweets_list = []
    for topic in topics:
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(topic).get_items()):
            if i>5:
                break

            # print('Attributes : \n')
            # print(inspect.getmembers(tweet, lambda a:not(inspect.isroutine(a))))

            tweets_list.append([topic ,tweet.date, tweet.url, tweet.content, tweet.username])
        
    tweets_df = pd.DataFrame(tweets_list, columns=['Tags/Keyword', 'Datetime', 'Tweet Id/URL', 'Text', 'Username'])
    return tweets_df

def cleansing_dataframe(df):

    df["Cleansed"] = df['Text'].apply(lambda text: remove_hashtag(text)) # Remove Hashtag
    df['Cleansed'] = df['Cleansed'].apply(lambda x: ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x).split())) # Remove URL, Mention
    df["Cleansed"] = df['Cleansed'].apply(lambda text: remove_punctuation(text)) # Remove Symbols
    df["Cleansed"] = list(map(lambda x: re.sub(r"\d+", "", x), df['Cleansed'].values.tolist())) # Remove Numbers
    df["Cleansed"] = list(map(lambda x: x.replace('\n', '') if '\n' in x else x, df['Cleansed'].values.tolist())) # remove \n
    df["Cleansed"] = [x.lower() for x in df['Cleansed'].values.tolist()] # Split Captial Words, and make all lowercase
    df["Cleansed"] = df['Cleansed'].apply(lambda text: removeStopwords(text)) # Remove Stopwords

    return df

def checkLongestTweet(df):
    list_longest_tweet = []

    for i in topics:
        try:
            temp_df = df.loc[df['Tags/Keyword'] == i]
            temp_cleansed = temp_df['Cleansed'].values.tolist()
            temp_username = temp_df['Username'].values.tolist()
            temp_list = []

            longest_cleansed = max(temp_cleansed, key=len)
            idx = temp_cleansed.index(longest_cleansed)
            username_of_longest = temp_username[idx]
            temp_list = [i, username_of_longest, longest_cleansed]
            list_longest_tweet.append(temp_list)
        except:
            print(i)

    longest_df = pd.DataFrame(list_longest_tweet, columns=['Tags/Keyword', 'Username', 'Cleansed'])
    return longest_df

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))

def remove_hashtag(sentence):
    global freq_hashtags
    texts = sentence.split()
    final_texts = []
    hashtags = []

    for i in texts:
        if '#' not in i:
             final_texts.append(i)
        else:
            word = checkHashtag(i)

            if type(word) != str:
                final_texts.append(word[0])
                word = word[-1]
                
            hashtags.append(word)
            
    all_hashtags.append(hashtags)
    freq_hashtags += hashtags
    return " ".join(final_texts)

def checkHashtag(word):
    if word[0] != '#':
        word = word.split('#')
        word[-1] = '#' + word[-1]

    return word
# print(remove_hashtag('Banjarmasin yang suka kain jarik dan suka dibungkus ada gak ya huhuhu #gaybjm #gaybanjarmasin #kainjarik #bungkus #gaykainjarik'))

def removeStopwords(kalimat):
    tokens = word_tokenize(kalimat)
    not_removed = []

    for t in tokens:
        if t not in all_stopwords and len(t)> 3:
            not_removed.append(t)
            countWords(t, 'Relevant')
        else:
            countWords(t, 'Irrelevant')

    return " ".join(not_removed)


def countWords(word, tipe):
    global total_words

    if tipe == 'Relevant':
        if word not in relevant_words:
            relevant_words[word] = 0
        
        relevant_words[word] += 1
           
    else:

        if word not in removed_words:
            removed_words[word] = 0
        
        removed_words[word] += 1

    total_words = total_words + 1

def createWordCloud(relevant_words):

    unique_string = (" ").join(relevant_words[:75])
    wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
    plt.style.use('seaborn-white')
    plt.figure(figsize=(20,10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("result\\wordcloud"+".png", bbox_inches='tight')

    return list(wordcloud.words_.keys())

def compare(data_to_compare, df, tipe):
    listnew = []

    if tipe == "Word":
        tipe = ["Cleansed", "Tags/Keyword"]
    else:
        tipe = ["Hashtag", "Username"]

    for index, value in df[tipe[0]].items():
        # print(index, 'x:', x, 'val:', value)
        try:
            if any(x in value for x in data_to_compare):
                listnew.append(df.loc[index, tipe[1]])
        except:
            pass

    return list(set(listnew))

def createNetworkGraph(list_of_sentences, list_of_mapping, filename):
    df_values = []
    count = 0

    # print('-----------')
    # print(list_of_sentences)
    # print('----------')
    # print(list_of_mapping)
    # print('----------')

    for i in list_of_mapping:
        for j in i:
            df_values.append([j, list_of_sentences[count]])

        count+=1
    
    df = pd.DataFrame(df_values, columns = ['Source', 'Target'])
    G = nx.from_pandas_edgelist(df, 'Source', 'Target') #Turn df into graph
    pos = nx.random_layout(G) #specify layout for visual

    f, ax = plt.subplots(figsize=(20, 10))
    plt.style.use('seaborn-pastel')
    nodes = nx.draw_networkx_nodes(G, pos, alpha=0.8)
    nodes.set_edgecolor('k')
    nx.draw_networkx_labels(G, pos, font_size=8)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.2)
    plt.savefig("result\\"+filename+".png", bbox_inches='tight')

def main():
    global total_words, all_hashtags

    # Start Timer
    start_time = time.time()
    str_start = time.ctime(start_time)
    print(str_start)

    # Scraping
    df = scrapTwitter(topics)

    # Scrap Retweet, Comments, Like. Komen aja kalo ga kepake
    list_url = df['Tweet Id/URL'].values.tolist()
    df['Retweet'], df['Comment'], df['Like'] = scrapOthers(list_url)

    # Cleansing Process
    df = cleansing_dataframe(df)

    # Hashtags
    final_hashtags = []
    for i in all_hashtags:
        if i == []:
            final_hashtags.append('-')
        else:
            final_hashtags.append(', '.join(i))

    df['Hashtag'] = final_hashtags
    hashtagCounter = collections.Counter(freq_hashtags)
    totalHashtag = list(hashtagCounter.values())
    dfHashtag = {'Hashtag': list(hashtagCounter.keys()),'Frequency': totalHashtag} 
    dfHashtag = pd.DataFrame.from_dict(dfHashtag).sort_values(by=['Frequency'], ascending=False)
    dfHashtag['Percentage'] = dfHashtag['Frequency'].apply(lambda x: str((x/sum(totalHashtag))*100)+ '%')

    # Check Longest Tweet
    longest_df = checkLongestTweet(df)

    # Counting Result to DF
    df_relevant = pd.DataFrame(list(relevant_words.items()), columns=['Words', 'Frequency']).sort_values(by=['Frequency'], ascending=False)
    df_relevant['Percentage'] = df_relevant['Frequency'].apply(lambda x: str((x/total_words)*100)+ '%')
    df_removed = pd.DataFrame(list(removed_words.items()), columns=['Words', 'Frequency']).sort_values(by=['Frequency'], ascending=False)
    df_removed['Percentage'] = df_removed['Frequency'].apply(lambda x: str((x/total_words)*100)+ '%')

    # Create Wordcloud
    wordclouds = createWordCloud(df_relevant['Words'].values.tolist())

    # Create Word Network Graph
    comparing_result = [compare(y, df, 'Word') for y in wordclouds]
    createNetworkGraph(wordclouds, comparing_result, 'word_network')

    # Create Actor Network Graph
    comparing_result = [compare(y, df, 'Actor') for y in dfHashtag['Hashtag'].values.tolist()[:5]]
    createNetworkGraph(dfHashtag['Hashtag'].values.tolist(), comparing_result, 'actor_network')

    # Prepare DF to excel
    df_excel = df.sample(frac = 1) # Shuffle Dataframe
    df_excel['Datetime'] = df_excel['Datetime'].apply(lambda x: pd.to_datetime(x).date()) # Str to Datetime
    with pd.ExcelWriter('result\\twitter.xlsx') as writer:  # pylint: disable=abstract-class-instantiated
        df_excel.to_excel(writer, sheet_name='Scraping Result', index=False)
        df_relevant.to_excel(writer, sheet_name='Relevant Words', index=False)
        df_removed.to_excel(writer, sheet_name='Irrelevant Words (Stopwords)', index=False)
        longest_df.to_excel(writer, sheet_name='Longest Tweet', index=False)
        dfHashtag.to_excel(writer, sheet_name='Hashtag Frequency', index=False)

    # Show
    img = mpimg.imread('result/wordcloud.png')
    imgplot = plt.imshow(img)
    plt.title("Word Cloud")
    img = mpimg.imread('result/word_network.png')
    imgplot = plt.imshow(img)
    plt.title("Word Network")
    img = mpimg.imread('result/actor_network.png')
    imgplot = plt.imshow(img)
    plt.title("Actor Network")

    # End Timer
    end_time = time.time()
    str_end = time.ctime(end_time)
    print(str_end)
    print("Runtime : %s minutes." % (round((end_time - start_time)/60)))

    plt.show()
    plt.close()

main()

# print(plt.style.available)

# import nltk
# nltk.download('stopwords')


# df["Cleansed"] = df['Text'].apply(lambda text: remove_hashtag(text)) # Remove Hashtag
# df['Cleansed'] = df['Cleansed'].apply(lambda x: ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x).split())) # Remove URL, Mention
# df["Cleansed"] = df['Cleansed'].apply(lambda text: remove_punctuation(text)) # Remove Symbols
# df["Cleansed"] = list(map(lambda x: re.sub(r"\d+", "", x), df['Cleansed'].values.tolist())) # Remove Numbers
# df["Cleansed"] = list(map(lambda x: x.replace('\n', '') if '\n' in x else x, df['Cleansed'].values.tolist())) # remove \n
# df["Cleansed"] = [x.lower() for x in df['Cleansed'].values.tolist()] # Split Captial Words, and make all lowercase
# df["Cleansed"] = df['Cleansed'].apply(lambda text: removeStopwords(text)) # Remove Stopwords


# kata_awal = "#Berita\nTerupdate Bejat, Kakek Asal Surabaya Diduga Cabuli Anak Difabel di Bawah Umur\n#kekerasanseksual\n#anakdibawahumur\nhttps://t.co/As4Rs2Z4KG"
# kata_akhir = remove_hashtag(kata_awal)
# print('')
# print('Before : ' + kata_awal)
# print('')
# print('After : ' + kata_akhir)
# print('')

# kata_awal = "Terupdate Bejat, Kakek Asal Surabaya Diduga Cabuli Anak Difabel di Bawah Umur https://t.co/As4Rs2Z4KG"
# kata_akhir = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",kata_awal).split())
# print('')
# print('Before : ' + kata_awal)
# print('')
# print('After : ' + kata_akhir)
# print('')

# kata_awal = "Terdakwa perkara fetish kain jarik, Gilang Aprilian Nugraha Pratama alias Gilang Bungkus divonis 5 tahun 6 bulan penjara"
# kata_akhir = re.sub(r"\d+", "", kata_awal)
# print('')
# print('Before : ' + kata_awal)
# print('')
# print('After : ' + kata_akhir)
# print('')

# kata_awal = "Terdakwa perkara fetish kain jarik Gilang Aprilian Nugraha Pratama alias Gilang Bungkus divonis  tahun  bulan penjara"
# kata_akhir = kata_awal.lower() 
# print('')
# print('Before : ' + kata_awal)
# print('')
# print('After : ' + kata_akhir)
# print('')

# kata_awal = "terdakwa perkara fetish kain jarik gilang aprilian nugraha pratama alias gilang bungkus divonis  tahun  bulan penjara"
# kata_akhir = removeStopwords(kata_awal)
# print('')
# print('Before : ' + kata_awal)
# print('')
# print('After : ' + kata_akhir)
# print('')
