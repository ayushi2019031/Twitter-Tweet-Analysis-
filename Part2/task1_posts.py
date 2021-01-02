
  
import xmltodict
import pprint
import json
import xml.etree.ElementTree as ET
d = 0
with open('stackoverflow.com/Posts.xml', 'r', encoding="utf-8") as file:
    data = file.read().replace("\n", "");
print("hello")
try:
	doc = xmltodict.parse(data)
	#pp.pprint(json.dumps(doc))
except Exception:
	print(Exception)
	doc = xmltodict.parse(data[1:])
#	pp.pprint(json.dumps(doc))
#pp.pprint(json.dumps(xmltodict.parse(data[3:])))

#print(doc)
k = json.dumps(doc)
listOfJsonStrings = []
for i in range(len(k)):
	if (k[i] == "{"):
		u = k.index("}", i)
		listOfJsonStrings.append(k[i: u + 1])
		i = u
	else:
		i+= 1
listOfJsonStrings = json.loads(k)		
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
# for key in listOfJsonStrings: 
# 	print(key)
# 	for tbt in listOfJsonStrings[key]:
# 		print(tbt + " \n")
# 		for ub in listOfJsonStrings[key][tbt]:
# 			print(listOfJsonStrings[key][] + "\n")
# #print(k)
from pymongo import MongoClient 

myclient = MongoClient("mongodb://localhost:27017/")  
   
# database  
db = myclient["Posts3"] 
tollection = db["data"]   

for str_ in listOfJsonStrings["posts"]["row"]:
	rec = tollection.insert_one(str_);
	# print(rec.inserted_id)
  
