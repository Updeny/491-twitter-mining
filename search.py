import twitter
import json
import config
from collections import Counter
from prettytable import PrettyTable


# Remove unicode from string
def removeUnicode(text):
    asciiText = ""
    for char in text:
        if(ord(char) < 128):
	    asciiText = asciiText + char
    return asciiText


# Retrieve authentication items
auth = twitter.oauth.OAuth(config.access_key, config.access_secret, config.api_key, config.api_secret)

tw = twitter.Twitter(auth = auth)

#SEARCH
q='@CocaCola'
count = 10
tweets = tw.search.tweets(q=q, count=count, lang='en')
texts = []
for status in tweets['statuses']:
    texts.append(status['text'])
print texts

print '======================='

words = []
for text in texts:
    for w in text.split():
        words.append(w)
print words

cnt = Counter(words)
pt = PrettyTable(field_names=['Word', 'Count'])
srtCnt = sorted(cnt.items(), key=lambda pair: pair[1], reverse=True)
for kv in srtCnt:
    pt.add_row(kv)
print(pt)

print '======================='

print 'Lexical Diversity'
print 1.0*len(set(words))/len(words)

