from flask import Flask, render_template, request, redirect, send_from_directory, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import json, os
from dotenv import load_dotenv
load_dotenv()
from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
    "email": os.getenv('email'),
    "password": os.getenv('password'),
})

def GetChatText(text):
    try:
        # If the first character is a number and a dot,remove it
        FirstChar = int(text[0])
        RtextWithDot = text.replace(str(FirstChar), '')
        Rtext = RtextWithDot.replace('.', '')

    except:
        Rtext = text
    if Rtext[0] != ' ':
        Rtext = ' ' + Rtext
    RequestText = 'Which subject is' + Rtext + '''?,If it's about math return 1,chinese 2,English 3,science 4,computer 5,music 6,art 7,PE 8,history 9,geography 10,civics 11,,other 12'''
    for data in chatbot.ask(RequestText):
        RespText = data['message']
    return RespText


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

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subject', methods=['POST'])
@limiter.limit("1/2second", override_defaults=True)
def subject():
    RequestJson = request.get_json()
    text = RequestJson['text']
    return GetChatText(text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',threaded=True)