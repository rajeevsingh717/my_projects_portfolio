######################## Tesla tweet analysis ##################################################################
import re
import pandas as pd
import string as str

def multiwordReplace(text, wordDic):
    """
    take a text and replace words that match a key in a dictionary with
    the associated value, return the changed text
    """
    rc = re.compile('|'.join(map(re.escape, wordDic)))
    def translate(match):
        return wordDic[match.group(0)]
    return rc.sub(translate, text)
    
stopword = ['a','about','above','after','again','against','all','am','an','and','any','are','as','at','be','because','been','before','being','below','between','both',
'but','by','cannot','could','did','does','doing','during','few','for','from','further','had','has','have','having','he','her','here','hers','herself','him',
'himself','his','how','i','if','in','into','is','it','its','itself','me','more','most','my','myself','no','nor','not','of','off','on','once','only','or',
'other','ought','our','ours','ourselves','out','over','own','same','to']

negative_words=['loss','lame','horrible','bad','bear','trap','punish',
'bubble','liar','depreciation','down','overvalue','risky',' slaughter','miss','sell','sweep','drop','low']

positive_words=['profit','good','nice','super','fun','bull','reward','take it','all in',
'hire','huge','gold','upgrade','unlimit','raise','top','up','hit','buy','earn','jump','hot','all in','pop']

# the dictionary has target_word : replacement_word pairs
wordDic = {
'raised': 'raise',
'overvalued': 'overvalue',
'bullish': 'bull',
'bearish': 'bear',
'bears':'bear',
'lower': 'low'}

    
tweets = []
users = []
pattern = re.compile("cvna", re.IGNORECASE)
pattern2 = re.compile("Aug 9th", re.IGNORECASE)
with open("cvnatweets.txt", encoding="utf8", errors='ignore') as tslt :
    for linenum , line in enumerate(tslt):
        if pattern.search(line) != None:          
                tweets.append((line.rstrip('\n')))
                                
        if pattern2.search(line) != None:          
                users.append((line.rstrip('\n')))

type(tweets)

tw = []
for i in range(0,len(tweets)):
    dum = re.sub('[0-9]', '', tweets[i])
    dum = re.sub(r"[-()'\"#$%/@;:<>{}`+=~|.!?,]", "", dum)
    dum = dum.lower()
    dum = multiwordReplace(dum, wordDic)    
    dum = dum.replace('ing',' ')
    dum = dum.replace('ed',' ')
    
    dumsplit = dum.split()
    filtered_dum = [word for word in dumsplit if word not in stopword]
    dum = ' '.join(filtered_dum)
    tw.append(dum)


################ Converting into data frame ################################################
tf = pd.DataFrame(tw)
tf.columns = ['normalized_tweet_Comments']
tf['poscnt'] =0
tf['negcnt'] =0



################ Finding list of common words with negative and positive ###################
listneg=[]
listpos=[]
i=0
for i in range(0,len(tf)):
    tfwords= tf.loc[i,'normalized_tweet_Comments']
    tfl = tfwords.split(' ')
    for l1 in tfl:
        for l2 in negative_words:
            if l2 == l1:
                listneg.append(l2)
    if len(listneg)!=0 :
        tf.loc[i,'negcnt'] = len(listneg)        
        listneg=[]
  
    for l1 in tfl:
        for l2 in positive_words:
            if l2 == l1:
                listpos.append(l2)
    if len(listpos)!=0 :    
        tf.loc[i,'poscnt'] = len(listpos)        
        listpos=[]

################Converting into data frame assigning columns to process further ###################
tfuser = pd.DataFrame(users)
tftweets = pd.DataFrame(tweets)
tfuser.columns = ['userdate']
tftweets.columns = ['tweets']

################ data parsing Creation of new data frame to get all the tweets, date, user in a table format
twdf=pd.DataFrame(columns=['user','dat','tweets'])
for i in range(0,len(tfuser)):
    inp = tfuser.loc[i,'userdate']
    pos = inp.find('Aug')
    usr = inp[0:pos]
    udate = inp[pos:len(inp)]
    twdf.loc[i,'user'] = usr
    twdf.loc[i,'dat'] = udate
    twdf.loc[i,'tweets'] = tftweets.loc[i,'tweets']
    
    
################ Joining the 2 dataframe ########################
finaldf = pd.concat([twdf,tf], axis=1)
finaldf['dat'] = '2018 ' + finaldf['dat']

################ create a new col set for market hr #######
markhrlist = []
for i in range(0,len(finaldf)) :
    sam = finaldf.loc[i,'dat']
    hr,mint = sam.replace('am','').replace('pm','').strip().split(',',1)[1].strip().split(':',1)
    hr,mint = int(hr),int(mint)
    if ((sam.find('am') > 0) & (((hr <= 9) & (mint<30)) | (hr<9))): markhr = 'pre-market'
    elif ((sam.find('pm') > 0) & (hr == 12)): markhr = 'in-market'    
    elif ((sam.find('pm') > 0) & (hr >= 4)): markhr = 'post-market'
    else : markhr = 'in-market'  
    markhrlist.append(markhr)

markhrlist = pd.DataFrame(markhrlist)
markhrlist.columns = ['markethour']
finaldf = pd.concat([finaldf,markhrlist], axis=1)


################ Removing not needed variables ##################
del(l1,l2,dum,dumsplit,filtered_dum,i,inp,line,linenum,listneg,listpos,
    negative_words,pos,positive_words,stopword,tf,tfl,tftweets,tfuser,tfwords,
    tw,twdf,tweets,udate,users,usr,wordDic)
##del(finaldf['dat'])
    
################ Reporting ######################################
len(finaldf.loc[(finaldf['poscnt']==0) & (finaldf['negcnt']==0)])
## Single Column group by - Count of all total tweets per user
finaldf.groupby('user').tweets.agg({'CountPerUser': 'count'}).sort_values('CountPerUser')

## multi Column group by - Count of total positive and negative tweets  per user
(finaldf.groupby('user')
    .agg({'poscnt': 'sum', 'negcnt': 'min'})
    .rename(columns={'poscnt': 'postot', 'negcnt': 'negtot'})
)

## checking specific user tweets
finaldf.loc[finaldf['user']=='MoneyisHoney',['tweets','poscnt','negcnt']]





