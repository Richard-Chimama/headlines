import feedparser

from flask import Flask

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
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1>Headlines </h1>
            <b>{0}</b> <br />
            <i>{1}</i> <br />
            <p>{2}</p> <br />
        </body>
    </html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))


if __name__=="__main__":
    app.run(port=5000,debug=True)
