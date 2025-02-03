from pymongo import MongoClient

# اتصال به MongoDB
client = MongoClient('localhost', 27017)
db = client['mydatabase']
collection = db['documents']

# افزودن داده‌های نمونه
documents = [
    {"title": "Sample Document 1", "content": "This is the content of sample document 1."},
    {"title": "Sample Document 2", "content": "This is the content of sample document 2."}
]

# اضافه کردن داده‌ها به کالکشن
collection.insert_many(documents)

# بررسی داده‌ها
results = collection.find()
for result in results:
    print(result)