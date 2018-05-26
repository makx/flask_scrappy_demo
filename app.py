import json
from flask import Flask
from flask import ( render_template, jsonify, request )
from flask_pymongo import PyMongo
from scrapy.crawler import CrawlerRunner
from demo_scraper import QuoteSpider
from scrapper import LoggerSpider
from pprint import pprint
import os


app = Flask('adquisicion')
app.config['MONGO_HOST'] = os.environ["MONGO_HOST"]
app.config['MONGO_DBNAME'] = os.environ["MONGO_COLLECTION"]
mongo = PyMongo(app)


crawl_runner = CrawlerRunner()      # requires the Twisted reactor to run
scrape_in_progress = False
scrape_complete = False

@app.route('/')
def hello_world():
    global scrape_in_progress
    global scrape_complete

    return render_template('index.html', scrape_complete=scrape_complete, scrape_in_progress=scrape_in_progress)


@app.route('/scrapp')
def scrapp():
    global scrape_in_progress
    global scrape_complete

    url_inicial= request.args.get('url')
    if not scrape_in_progress:
        scrape_in_progress = True
        eventual = crawl_runner.crawl(LoggerSpider, url_inicial=url_inicial)
        eventual.addCallback(finished_scrape)
    
    return render_template('scrapp.html', scrape_complete=scrape_complete, scrape_in_progress=scrape_in_progress)

@app.route('/status')
def get_status():
    global scrape_in_progress
    count = mongo.db.urls.count()

    latestCursor = mongo.db.urls.find().sort("_id", -1).limit(1)
    latestArray = []
    for doc in latestCursor :
        latestArray.append({
            "title": doc["title"],
            "url": doc["url"],
            "description": doc["description"]
        })
    return jsonify({
        'scrapping': scrape_in_progress,
        'count': count,
        'newAdded': latestArray
    })

@app.route('/stopspider')
def stop_spider():
    crawl_runner.stop()
    return jsonify({
        "status": "ok"
    })

def finished_scrape(null):
    global scrape_complete
    global scrape_in_progress
    scrape_in_progress = False
    scrape_complete = True

if __name__=='__main__':
    from sys import stdout
    from twisted.logger import globalLogBeginner, textFileLogObserver
    from twisted.web import server, wsgi
    from twisted.internet import endpoints, reactor

    globalLogBeginner.beginLoggingTo([textFileLogObserver(stdout)])

    root_resource = wsgi.WSGIResource(reactor, reactor.getThreadPool(), app)
    factory = server.Site(root_resource)
    http_server = endpoints.TCP4ServerEndpoint(reactor, 9000)
    http_server.listen(factory)

    reactor.run()