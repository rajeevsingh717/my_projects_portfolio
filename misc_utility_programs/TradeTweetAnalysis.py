import re
import pandas as pd
import string as str
       

alltweetusr = []
alltweetcmnts = []
flg=1
regex = r"\w\w\w \d\d\w\w, "
with open("tweets.txt",encoding='utf8',errors="ignore") as twts :
    for  line in twts:
        if  re.search(regex, line):
            alltweetusr.append(line.rstrip('\n'))
                
        if flg == 0:
            alltweetcmnts.append(line.rstrip('\n'))
            flg=1

        if re.search(regex, line):
            flg = 0       

alltweetusr, alltweetcmnts = pd.DataFrame(alltweetusr), pd.DataFrame(alltweetcmnts)
alltweetusr.columns = ['user']
alltweetcmnts.columns = ['tweets']

############### Creating user and date column
twdf=pd.DataFrame(columns=['user','dat'])
for i in range(0,len(alltweetusr)):
    inp = alltweetusr.loc[i,'user']
    pos = inp.find('Aug')
    usr = inp[0:pos]
    udate = inp[pos:len(inp)]
    twdf.loc[i,'user'] = usr
    twdf.loc[i,'dat'] = udate
finaldf = pd.concat([twdf,alltweetcmnts], axis=1) 

############### Creating final dataframe after cominging USER,DATE and comments  
shrs = pd.DataFrame(columns=['shareslisted'])
for i in range(0,len(finaldf)):
     shares = re.findall(r'\$\w+', finaldf.loc[i,'tweets'])
     shares = ", ".join(shares)
     shrs.loc[i,'shareslisted'] = shares
finaldf = pd.concat([finaldf,shrs], axis=1)

############ Creating seperate shares list for all the shares for inividual users
temp_df = pd.DataFrame()
for i in range(0,len(finaldf)):
    tem_s = finaldf.loc[i,'shareslisted']    
    tem_l = tem_s.split(',')
    tem_df = pd.DataFrame(tem_l)
    tem_df_t = tem_df.transpose()
    temp_df = pd.concat([temp_df,tem_df_t], axis=0 ,ignore_index=True)
finaldf = pd.concat([finaldf,temp_df], axis=1)  

finaldf.columns = ['user', 'dat', 'tweets', 'shareslisted', 'share1', 'share2', 
'share3', 'share4', 'share5', 'share6', 'share7', 'share8']

################ create a new col set for market hr #######
finaldf['dat'] = '2018 ' + finaldf['dat']
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



############ Removing unwanted variables ##############################
del(alltweetcmnts ,alltweetusr ,flg ,i,inp,
line, pos,regex,shares,shrs ,tem_df,tem_df_t , tem_l ,tem_s, 
temp_df,twdf,twts,udate,usr)


############# Reporting ###################
finaldf[['user','share1']].groupby('share1').count() ## group by share1
finaldf.groupby(['user','share1']).tweets.agg({'countpershare' : 'count'}).sort_values('countpershare')
finaldf.groupby('user').tweets.agg({'countperuser':'count'}).sort_values('countperuser') ## group by share1

finaldf.loc[finaldf['share1']=='$TSLA','tweets']
print(finaldf.loc[finaldf['user']=='Trading4Living','tweets'])


