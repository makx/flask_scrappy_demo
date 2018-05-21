

settings = {
    'CLOSESPIDER_TIMEOUT': 20,
    'ITEM_PIPELINES': {
        'pipelines.MongoPipeline': 1,
    },
    'MONGO_URI': 'mongodb',
    'MONGO_DATABASE': 'adquisicion_db'
}