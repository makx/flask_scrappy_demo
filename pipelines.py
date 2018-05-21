import pymongo

class MongoPipeline(object):
    collection_name= 'urls'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri= mongo_uri
        self.mongo_db= mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )
    
    def open_spider(self, spider):
        print('es el open de la spider')
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        print('entra al process')
        self.db[self.collection_name].insert_one(dict(item))
        return item
    
    def close_spider(self, spider):
        print('funciona el close')
        self.client.close()

    # def __init__(self, mongo_uri, mongo_db):
    #     self.mongo_uri = mongo_uri
    #     self.mongo_db = mongo_db

    # @classmethod
    # def from_crawler(cls, crawler):
        ## pull in information from settings.py
        # return cls(
        #     mongo_uri=crawler.settings.get('MONGO_URI'),
        #     mongo_db=crawler.settings.get('MONGO_DATABASE')
        # )

    # def open_spider(self, spider):
    #     ## initializing spider
    #     ## opening db connection
    #     self.client = pymongo.MongoClient(self.mongo_uri)
    #     self.db = self.client[self.mongo_db]

    