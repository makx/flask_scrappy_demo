import json
from flask import Flask
from flask import ( render_template, jsonify )
from flask_pymongo import PyMongo
from scrapy.crawler import CrawlerRunner
from demo_scraper import QuoteSpider
from scrapper import LoggerSpider
from pprint import pprint

app = Flask('adquisicion')
app.config['MONGO_HOST'] = 'mongodb'
app.config['MONGO_DBNAME'] = 'adquisicion_db'
mongo = PyMongo(app)




crawl_runner = CrawlerRunner()      # requires the Twisted reactor to run
quotes_list = []                    # store quotes
scrape_in_progress = False
scrape_complete = False
limit = 10

@app.route('/')
def hello_world():
    return 'Scrapper para trabajo finalli'

@app.route('/pruebajson2')
def testmongo():
    # url_name = mongo.db.urls.first({'name': 'clarin'})
    sample = mongo.db.urls.find({})
    for url in sample:
        pprint(url)
    return 'la url ea: '

# @app.route('/pruebajson')
# def getjson():
#     with open('./urls_to_scrap.json') as jsondata:
#         d = json.load(jsondata)
#         jsondata.close
#         pprint(d)
#         return json.dumps(d)

@app.route('/scrapp')
def scrapp():
    global scrape_in_progress
    global scrape_complete

    if not scrape_in_progress:
        scrape_in_progress = True
        # start the crawler and execute a callback when complete
        eventual = crawl_runner.crawl(LoggerSpider)
        eventual.addCallback(finished_scrape)
    
    return render_template('index.html', scrape_complete=scrape_complete, scrape_in_progress=scrape_in_progress)

# @app.route('/gotoscrapp')
# def runScrapper():
#     global scrape_complete
#     global scrape_in_progress
#     global quotes_list
#     global limit
#     url = mongo.db.urls.find_one({'visit': False})
#     eventual = crawl_runner.crawl(QuoteSpider, quotes_list=quotes_list, mongo=mongo, url=url)
#     eventual.addCallback(finished_scrape)
#     # result= mongo.db.urls.update_one({'url':url['url']}, {'$set': {'visit': False}})
#     # while not scrape_complete:
#     #     url = mongo.db.urls.find_one({'visit': True})
#     #     scrape_in_progress = True
#     #     if (url is None) | ((limit-1) == 0):
#     #         scrape_in_progress= False
#     #         scrape_complete= True
#     #     else:
#     #         eventual = crawl_runner.crawl(QuoteSpider, quotes_list=quotes_list, mongo=mongo, url=url)
#     #         eventual.addCallback(finished_scrape)
#     #         result= mongo.db.urls.update_one({'url':url['url']}, {'$set': {'visit': False}})
#     #     limit -= 1
#     # scrape_complete = True
#     return 'Terminó tuti'

@app.route('/crawl')
def crawl_for_quotes():
    """
    Scrapear títulos de noticias
    """

    if not scrape_in_progress:
        scrape_in_progress = True
        global quotes_list
        # start the crawler and execute a callback when complete
        eventual = crawl_runner.crawl(QuoteSpider, quotes_list=quotes_list)
        eventual.addCallback(finished_scrape)
        return 'SCRAPING'
    elif scrape_complete:
        return 'SCRAPE COMPLETE'
    return 'SCRAPE IN PROGRESS'

@app.route('/results')
def get_results():
    """
    Get the results only if a spider has results
    """
    global scrape_complete
    if scrape_complete:
        return json.dumps(quotes_list)
    return 'Scrape Still Progresssss'

def finished_scrape(null):
    pprint('Callback fin del scrapping')
    global scrape_complete
    scrape_complete = True

@app.route('/status')
def get_status():
    global scrape_complete
    count = mongo.db.urls.count()
    return jsonify({
        'scrapping': scrape_complete,
        'cantidad': count
    })

if __name__=='__main__':
    from sys import stdout
    from twisted.logger import globalLogBeginner, textFileLogObserver
    from twisted.web import server, wsgi
    from twisted.internet import endpoints, reactor

    # start the logger
    globalLogBeginner.beginLoggingTo([textFileLogObserver(stdout)])

    # start the WSGI server
    root_resource = wsgi.WSGIResource(reactor, reactor.getThreadPool(), app)
    factory = server.Site(root_resource)
    http_server = endpoints.TCP4ServerEndpoint(reactor, 9000)
    http_server.listen(factory)

    # start event loop
    reactor.run()