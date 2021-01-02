from pymongo import MongoClient 
import json
from collections import defaultdict
import matplotlib.pyplot as plt


myclient = MongoClient("mongodb://localhost:27017/")  
   
# database  
db = myclient["Posts3"] 
tollection = db["data"]   

print(tollection.find().count())

ref_list = defaultdict(int)

for stri in db.data.find():
	#print(stri)
	ayushi = stri.get("@Tags")
	if (ayushi != None):
		l = ayushi[1:len(ayushi) - 1].split("><")
		for k in l:
			ref_list[k] += 1;

# print(ref_list)
final_list = sorted(ref_list.items(),key=lambda kv : kv[1],reverse=True)

res = final_list[:10]

print(res)
list1, list2 = zip(*res)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.bar(list1, list2)
plt.show()
