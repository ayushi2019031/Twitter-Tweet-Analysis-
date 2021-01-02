from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 

from pymongo import MongoClient 
import json
from collections import defaultdict
import matplotlib.pyplot as plt


myclient = MongoClient("mongodb://localhost:27017/")  
   
# database  
db = myclient["Posts3"] 
tollection = db["data"]   

  
comment_words = '' 
stopwords = set(STOPWORDS) 
stopwords.add("https")
stopwords.add("P")
stopwords.add("code")

i = 0; 
# iterate through the csv file 
try:
    t = db.data.find()
    for stri in t: 
        try:
            i += 1; 
            print(i)
            print(stri) 
            # if (i  == 1000):
            #     break;
           # print("baaa");
              #pecaste each val to string 
            val = stri.get("@Body")
            if (val != None):
          
            # split the value 
                tokens = val.split() 
                  
                # Converts each token into lowercase 
                for j in range(len(tokens)): 
                    tokens[j] = tokens[j].lower() 
                  
                comment_words += " ".join(tokens)+" "
        except:
            break;
except:
    print("Ok")  
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 