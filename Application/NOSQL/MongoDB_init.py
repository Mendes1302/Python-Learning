import pymongo
import urllib 


cluster = pymongo.MongoClient("your-url)
db = cluster["first"]


data = { "_id": 0, "Lucas": 31, "Debora": 32, "Helena": 34, "Joaquim": 36}
collection = db["first"]
#Insert
collection.insert_one(data)

#delete
collection.delete_one({"Debora":32})


#show
results = collection.find({"Lucas":31})
for result in results:
    print(result)


print("END")