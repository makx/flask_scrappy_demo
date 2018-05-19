class MongoPipeline(object):
    def process_item(self, item, spider):
        print('entra al process')
        return item
    
    def close_spider(self, spider):
        ## clean up when spider is closed
        print('funciona el close')
    def open_spider(self, spider):
        print('es el open de la spider')

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

    