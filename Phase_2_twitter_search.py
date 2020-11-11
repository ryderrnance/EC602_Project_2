import tweepy #https://github.com/tweepy/tweepy
import json
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import re
from nltk.tokenize import WordPunctTokenizer
from google.oauth2 import service_account
from tabulate import tabulate
from termcolor import colored, cprint 

credentials = service_account.Credentials.from_service_account_file(r'C:\Users\Ryder\Documents\602_Project2\NLP_key2.json')

#####Enter your credentials here#####



def broom(tweet):
    '''
        Helper function that cleans up the tweets to make them easier to process
    '''
    #print('sweeping')
    user_removed = re.sub(r'@[A-Za-z0-9]+','',tweet)
    #print(user_removed)
    link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
    number_removed = re.sub('[^a-zA-Z]', ' ', link_removed)
    lower_case_tweet= number_removed.lower()
    tok = WordPunctTokenizer()
    words = tok.tokenize(lower_case_tweet)
    clean_tweet = (' '.join(words)).strip()
    #print(clean_tweet)
    return clean_tweet


def get_sentiment_score(tweet):
    ## use explicit definition of client credential variables bs otherwise it didnt work
    client = language.LanguageServiceClient(credentials=credentials)
    document = types\
               .Document(content=tweet,
                         type=enums.Document.Type.PLAIN_TEXT)
    sentiment_score = client\
                      .analyze_sentiment(document=document)\
                      .document_sentiment\
                      .score
    return sentiment_score



search_term = input('Enter the handle of the customer service line: ')
orig_date = '2020-10-01' #input('Enter the origin date for the search to begin')
results = input('How many tweets should I look at(max 200): ')
fetching = int(results)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
#api.search('@southwestair')

tweets = tweepy.Cursor(api.search,q=search_term,lang='en',since=orig_date).items(fetching)
tweets2 = tweepy.Cursor(api.search,q=search_term,lang='en',since=orig_date).items(fetching)
#tweets3 = tweepy.Cursor(api.search,q=search_term,lang='en',since=orig_date).items(20)

#for tweet in tweets: #   print(tweet)

#for tweet in tweets:
#    cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))
#print(tweets)
#print(cleaned_tweet)

#twt_list = [[twt.user.screen_name, twt.text] for twt in tweets]

cleaned_text = [broom(twt.text) for twt in tweets2]

users  = [twt.user.screen_name for twt in tweets]

scores = [get_sentiment_score(twt) for twt in cleaned_text]

#for twt in tweets2:  ####printing here seems to modify the tweets 2 so the later code
#wont run
#    print(twt.user.screen_name)

#print(tweets2)
#print(twt_list);

#print(clean_tweets(tweets))

#cleaned_text = [broom(twt) for twt in tweets2]

#cleaned_text = []

#for twt in tweets2:
   # print('running thru tweets')
    #print(twt)
    #cleaned_text.append( broom(twt.text))

headers = ['Twitter Handle', 'Sentiment', 'UTF-8 Encoded Tweet']

fulldata = [(users[x], scores[x]) for x in range(len(users))]

#print(cleaned_text)
#print(users)
#print(scores)

print(tabulate(fulldata, headers=headers))
print
##Calculate Statistics##
average = sum(scores)/len(scores)

print('The average sentiment score is ', "{:.2f}".format(average))




# Code written by Ryder nance, with referenc and some snippets taken from the following:
# freecodecamp.org
