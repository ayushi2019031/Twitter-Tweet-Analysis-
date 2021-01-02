from pymongo import MongoClient 
import json
from collections import defaultdict
import matplotlib.pyplot as plt


myclient = MongoClient("mongodb://localhost:27017/")  
   
# database  
db = myclient["Tags3"] 
tollection = db["data"]   

print(tollection.find().count())

ref_list = defaultdict(int)

for stri in db.data.find():
    #print(stri)
    ayushi = stri.get("@TagName")
    if (ayushi != None):
        ref_list[ayushi] += int(stri.get("@Count"));


final_list = sorted(ref_list.items(),key=lambda kv : kv[1],reverse=True)

res = final_list[:15]

print(res)
list1, list2 = zip(*res)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(list1, list2)

ax.set_xticklabels(list1, rotation=0, fontsize=100)
# ax.xlabel("Followers")
ax.set_yticklabels(list2, rotation=0, fontsize=100)

plt.show()
