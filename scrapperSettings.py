import os

settings = {
    'CLOSESPIDER_TIMEOUT': os.environ["SPIDER_TIME_LIMIT"],
    'ITEM_PIPELINES': {
        'pipelines.MongoPipeline': 1,
    },
    'MONGO_URI': os.environ["MONGO_HOST"],
    'MONGO_DATABASE': os.environ["MONGO_COLLECTION"]
}