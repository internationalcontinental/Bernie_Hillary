import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import folium
#import numpy as np
from folium import plugins
#wdir=r'D:/Documents/DataIncubator'
tweets_data_path = 'primaryNY1.txt'
tweets_data = []
for line in open(tweets_data_path):
  try: 
    tweet = json.loads(line)
    tweets_data.append(tweet)
  except:
    pass
print len(tweets_data)
###    

tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet.get('text',None), tweets_data)
tweets['lang'] = map(lambda tweet: tweet.get('lang', None),tweets_data)
tweets['long'] = list(map(lambda tweet: tweet['coordinates']['coordinates'][0] if tweet['coordinates'] != None else None, tweets_data))
tweets['lat'] = list(map(lambda tweet: tweet['coordinates']['coordinates'][1]
                        if tweet['coordinates'] != None else None, tweets_data))

#
def words(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False
#    
tweets['sanders'] = tweets['text'].apply(lambda tweet: words('sanders', tweet))
tweets['clinton'] = tweets['text'].apply(lambda tweet: words('clinton', tweet))
#tweets['#feelthebern'] = tweets['text'].apply(lambda tweet: word_in_text('#feelthebern', tweet))
#tweets['#hillary2016'] = tweets['text'].apply(lambda tweet: word_in_text('#hillary2016', tweet))


print tweets['clinton'].value_counts()[True]
print tweets['sanders'].value_counts()[True]

count = 0
for l in tweets_data:
    if l['coordinates'] is not None:
        count +=1
        
print(float(count)/float(len(tweets_data))*100)


ny_dems = ['Sanders', 'Clinton']
tweets_ny_dems = [tweets['sanders'].value_counts()[True], tweets['clinton'].value_counts()[True]]

x_pos = list(range(len(ny_dems)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_ny_dems, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of Tweets', fontsize=15)
ax.set_title('Sanders vs. Clinton', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(ny_dems)
plt.grid()
plt.savefig('sand_clint.png')
ny_dem= folium.Map(location=[39.0558,-125], zoom_start=4)

#[folium.CircleMarker(location=[l['coordinates']['coordinates'][1],
#                               l['coordinates']['coordinates'][0]],
#                     radius=10,color="red", popup = l['text']).add_to(ny_dem)
#for l in tweets_data if l['coordinates']
#          is not None]
ny_dem.add_children(plugins.HeatMap([[l['coordinates']['coordinates'][1],l['coordinates']['coordinates'][0]] 
 for l in tweets_data if l['coordinates'] is not None ]))
ny_dem.save("./NY_primq.html")
ny_dem