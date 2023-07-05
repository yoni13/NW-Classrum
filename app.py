from flask import Flask, render_template, request, redirect, send_from_directory, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from connectgpt import GetChatText
import json, os
from dotenv import load_dotenv
load_dotenv()

from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://yoni:"+os.getenv('passwd')+"@cluster0.o0k9job.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[],
    storage_uri="memory://",
)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/inputarea')
def index():
    return render_template('inputarea.html')

@app.route('/subject', methods=['POST'])
@limiter.limit("1/2second", override_defaults=True)
def subject():
    RequestJson = request.get_json()
    text = RequestJson['text']
    return GetChatText(text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',threaded=True)