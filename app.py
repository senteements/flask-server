import dotenv
import os
import sys
from flask import Flask
from flask import request
from flask import jsonify
import workingscript

dotenv.load_dotenv()

CK = os.getenv('CONSUMER_KEY')
CS = os.getenv('CONSUMER_SECRET')
AT = os.getenv('ACCESS_TOKEN')
ATS = os.getenv('ACCESS_TOKEN_SECRET')

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome"


@app.route('/analyze')
def analyze():
    query = request.args.get('query')
    count = request.args.get('count')
    tweetsjson = workingscript.getAnalysis(query=query, count=count, ck = CK,cs = CS,at = AT,ats = ATS)
    print("...tweets fetched!")
    if (tweetsjson == None or (not tweetsjson)):
        errors = []
        errors.append({'text': "something went wrong!"})
        return jsonify(errors)
    return jsonify(tweetsjson)


if (__name__ == "__main__"):
    app.run()

#  Werkzeug, MarkupSafe, Jinja2, itsdangerous, click, Flask
# chardet, idna, urllib3, certifi, requests, oauthlib, requests-oauthlib, six, PySocks, tweepy
# nltk, textblob
# python-dotenv
# gunicorn
