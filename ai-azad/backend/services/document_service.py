# backend/services/document_service.py

from utils.db_utils import connect_mongo, connect_elasticsearch, connect_redis

def add_document(title, content):
    db = connect_mongo()
    collection = db['tax']

    try:
        document = {"title": title, "content": content}
        inserted_doc = collection.insert_one(document)

        # ذخیره در ElasticSearch
        es = connect_elasticsearch()
        es.index(index="tax", id=str(inserted_doc.inserted_id), body=document)

        # ذخیره در Redis
        r = connect_redis()
        r.set(f'document:{title}', content)

        return {"message": "Document added successfully."}
    except Exception as e:
        return {"message": f"Error adding document: {str(e)}"}

def get_documents():
    db = connect_mongo()
    collection = db['tax']

    results = list(collection.find({}, {"_id": 0}))
    return results

def update_document(title, new_content):
    db = connect_mongo()
    collection = db['tax']

    try:
        collection.update_one({"title": title}, {"$set": {"content": new_content}})

        # به‌روزرسانی در ElasticSearch
        es = connect_elasticsearch()
        doc_id = str(collection.find_one({"title": title})['_id'])
        es.index(index="tax", id=doc_id, body={"title": title, "content": new_content})

        # به‌روزرسانی در Redis
        r = connect_redis()
        r.set(f'document:{title}', new_content)

        return {"message": "Document updated successfully."}
    except Exception as e:
        return {"message": f"Error updating document: {str(e)}"}

def delete_document(title):
    db = connect_mongo()
    collection = db['tax']

    try:
        collection.delete_one({"title": title})

        # حذف از ElasticSearch
        es = connect_elasticsearch()
        es.delete_by_query(index="tax", body={"query": {"match": {"title": title}}})

        # حذف از Redis
        r = connect_redis()
        r.delete(f'document:{title}')

        return {"message": "Document deleted successfully."}
    except Exception as e:
        return {"message": f"Error deleting document: {str(e)}"}