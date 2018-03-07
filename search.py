import twitter
import config
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

# Retrieve authentication items
auth = twitter.oauth.OAuth(config.auth_key, config.auth_secret, config.consumer_key, config.consumer_secret)
tw = twitter.Twitter(auth = auth)

# Search twitter for @CocaCola's most popular tweets
q = 'from:CocaCola'
count=10
tweets = tw.search.tweets(q=q, count=count, lang='en', result_type='popular')
texts=[]

print 'Sentiment Analysis for @CocaCola\'s Most Popular Tweets:'
print '--------------------------------------------------------------------------'

# Sentiment analysis
for status in tweets['statuses']:
    texts.append(status['text'])
    print 'Tweet:'
    print '\t' + status['text'].encode('utf-8')
    vs = vaderSentiment(status['text'].encode('utf-8'))
    print 'Sentiment analysis:'
    print '\t' + str(vs['compound'])
    print '--------------------------------------------------------------------------'

print '\nLexical Analysis for @CocaCola\'s Most Popular Tweets:'
print '--------------------------------------------------------------------------'

# Lexical analysis
for text in texts:
    print 'Tweet:'
    print '\t' + text.encode('utf-8')
    words = []
    for w in text.split():
        words.append(w)
    print 'Lexical diversity:'
    print '\t' + str(1.0*len(set(words))/len(words))
    print '--------------------------------------------------------------------------'


# Search twitter for @Pepsi's most popular tweets
q = 'from:Pepsi'
count=10
tweets = tw.search.tweets(q=q, count=count, lang='en', result_type='popular')
texts=[]

print '\nSentiment Analysis for @Pepsi\'s Most Popular Tweets:'
print '--------------------------------------------------------------------------'

# Sentiment analysis
for status in tweets['statuses']:
    texts.append(status['text'])
    print 'Tweet:'
    print '\t' + status['text'].encode('utf-8')
    vs = vaderSentiment(status['text'].encode('utf-8'))
    print 'Sentiment analysis:'
    print '\t' + str(vs['compound'])
    print '--------------------------------------------------------------------------'

print '\nLexical Analysis for @Pepsi\'s Most Popular Tweets:'
print '--------------------------------------------------------------------------'

# Lexical analysis
for text in texts:
    print 'Tweet:'
    print '\t' + text.encode('utf-8')
    words = []
    for w in text.split():
        words.append(w)
    print 'Lexical diversity:'
    print '\t' + str(1.0*len(set(words))/len(words))
    print '--------------------------------------------------------------------------'
