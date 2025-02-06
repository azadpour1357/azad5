# backend/utils/db_utils.py

from pymongo import MongoClient
from elasticsearch import Elasticsearch
import redis
import psycopg2

def connect_mongo():
    client = MongoClient(
        "mongodb://root:example@mongo:27017/",
        serverSelectionTimeoutMS=5000
    )
    db = client['ai-tax-azad']
    collection = db['tax']

    # ایجاد اندیس روی عنوان
    collection.create_index("title")

    return db

def connect_elasticsearch():
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
    return es

def connect_redis():
    r = redis.Redis(host='redis', port=6379, db=0)
    return r

def connect_postgres():
    conn = psycopg2.connect(
        dbname='ai_tax_azad',
        user='admin',
        password='admin123',
        host='postgres'
    )
    return conn