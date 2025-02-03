from pymongo import MongoClient
import psycopg2
from elasticsearch import Elasticsearch
import redis
from utils.db_utils import connect_mongo, connect_postgres, connect_elasticsearch, connect_redis
from models.bert_model import classify_text

def perform_search(query):
    # MongoDB connection
    db = connect_mongo()
    collection = db['documents']
    
    mongo_results = collection.find({"title": {"$regex": query, "$options": "i"}})
    mongo_docs = [{"title": result["title"], "content": result["content"]} for result in mongo_results]

    # PostgreSQL connection
    conn = connect_postgres()
    cursor = conn.cursor()

    postgres_query = "SELECT * FROM documents WHERE title ILIKE %s"
    cursor.execute(postgres_query, (f"%{query}%",))
    postgres_results = cursor.fetchall()

    postgres_docs = [{"title": result[0], "content": result[1]} for result in postgres_results]
    cursor.close()
    conn.close()

    # ElasticSearch connection
    es = connect_elasticsearch()
    res = es.search(index="documents", body={"query": {"match": {"title": query}}})
    es_docs = [hit["_source"] for hit in res['hits']['hits']]

    # Redis connection
    r = connect_redis()
    redis_title = r.get(f'document:{query}:title')
    redis_content = r.get(f'document:{query}:content')
    redis_docs = []
    if redis_title and redis_content:
        redis_docs.append({"title": redis_title.decode('utf-8'), "content": redis_content.decode('utf-8')})

    # Classify documents using BERT
    classified_docs = []
    for doc in mongo_docs + postgres_docs + es_docs + redis_docs:
        classification = classify_text(doc['content'])
        classified_docs.append({**doc, 'classification': classification})

    return classified_docs