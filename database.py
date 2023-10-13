from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['twitter_db']
trends_collection = db['trends']

def get_filtered_trends(keyword=None):
    trends = list(trends_collection.find({}))
    if keyword:
        trends = [trend for trend in trends if keyword.lower() in trend['name'].lower()]
    return trends
