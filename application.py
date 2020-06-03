import feedparser

from flask import Flask, render_template

app = Flask(__name__)

#the variable hold the RSS feed URL
RSS_FEED = {'bbc':"http://feeds.bbci.co.uk/news/rss.xml",
            'cnn':"http://rss.cnn.com/rss/edition.rss",
            'fox':"https://feeds/foxnews.com/foxnews/latest",
            'iol':"http://www.oil.co.za/cmlink/1.640",
            'zssj':"https://scholarship.law.cornell.edu/zssj"}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEED[publication])
    return  render_template("index.html", articles=feed['entries'])       


if __name__=="__main__":
    app.run(port=5000,debug=True)
