# backend/services/search_service.py

from utils.db_utils import connect_mongo, connect_elasticsearch, connect_redis
from models.roberta_model import classify_text

def perform_search(query):
    # جستجو در MongoDB
    db = connect_mongo()
    collection = db['tax']
    mongo_results = collection.find({"title": {"$regex": query, "$options": "i"}})
    mongo_docs = [{"title": doc["title"], "content": doc["content"]} for doc in mongo_results]

    # جستجو در ElasticSearch
    es = connect_elasticsearch()
    res = es.search(index="tax", body={"query": {"match": {"title": query}}})
    es_docs = [hit["_source"] for hit in res['hits']['hits']]

    # کش کردن نتایج در Redis
    r = connect_redis()
    cache_key = f"search:{query}"
    cached_results = r.get(cache_key)

    if cached_results:
        return json.loads(cached_results)

    # طبقه‌بندی متن با RoBERTa
    classified_docs = []
    for doc in mongo_docs + es_docs:
        classification = classify_text(doc['content'])
        classified_docs.append({**doc, 'classification': classification})

    # ذخیره نتایج در Redis
    r.set(cache_key, json.dumps(classified_docs), ex=3600)

    return classified_docs