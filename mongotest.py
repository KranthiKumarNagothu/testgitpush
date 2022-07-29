import pymongo

client = pymongo.MongoClient("mongodb+srv://KranthiKumarNagothu:Kranthi123@cluster0.w8qep1f.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Kranthi Kumar",
    "email":"knagothu@gitam.in",
    "surname":"Nagothu"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)