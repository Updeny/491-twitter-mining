# CMSC 491-01, Spring 2018
# Dr. George Ray
# Project 1: Social Media Mining Twitter
# Group 7: 
#   Anna Aladiev 
#   Zachary Elliott 
#   Sean J. Jeong    
#   Wyatt Schweitzer          
#   Adam Snyder         
##################################################################################
# Our group chose to utilize the search API because it enabled us to retrieve 
# tweets instantly, as opposed to the stream API which at times required a 10
# minute wait. Overall, since this was a smaller-scale project, either API could 
# have been used to achieve similar results, but in the interest of waiting time, 
# we chose the search API. 
##################################################################################

import twitter
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
from prettytable import PrettyTable 		

def removeUnicode(text):
        asciiText = ""
        for char in text:
            if (ord(char) < 128):
                asciiText = asciiText + char
        return asciiText

# CONNECT TO TWITTER 
# FILL IN TWITTER TEST CREDENTIALS IN PLACE OF EMPTY STRING VALUES
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

tw = twitter.Twitter(auth=auth)


# RETRIEVE 25 COCA COLA AND 25 PEPSI TWEETS
q = ['CocaCola', 'Pepsi']
tables = []
count = 25
tweets = tw.search.tweets(q=q, count=count, lang='en')
texts = []
sentim = []

for x in range(0, len(q)):
	tables.append(PrettyTable())
	tables[x].field_names = [q[x] + " Tweets", "Sentiment Analysis", "Lexical Analysis"]

	# CALCULATE SENTIMENT ANALYSIS OF TWEET
	for status in tweets['statuses']:
	    texts.append(status["text"])
	    vs = vaderSentiment(status["text"].encode('utf-8'))
	    sentim.append(str(vs['compound']))

	# CALCULATE LEXICAL DIVERSITY OF EACH TWEET
	num = 0
	for text in texts:
	    words = []
	    string = ""
	    for w in text.split():
	        words.append(w)
	    	string += w + " "
	    tables[x].add_row([string, sentim[num], 1.0*len(set(words))/len(words)])
	    num = num + 1

	# DISPLAY EACH TWEET, SENTIMENT ANALYSIS, AND LEXICAL DIVERSITY 
	print(tables[x])