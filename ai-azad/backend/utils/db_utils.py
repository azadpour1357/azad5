from pymongo import MongoClient
import psycopg2
from elasticsearch import Elasticsearch
import redis

def connect_mongo():
    client = MongoClient('localhost', 27017)
    db = client['mydatabase']
    return db

def connect_postgres():
    conn = psycopg2.connect(
        dbname='mydatabase',
        user='myuser',
        password='mypassword',
        host='postgres'
    )
    return conn

def connect_elasticsearch():
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
    return es

def connect_redis():
    r = redis.Redis(host='redis', port=6379, db=0)
    return r