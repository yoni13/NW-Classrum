from flask import Flask, render_template, request, redirect, send_from_directory, abort
import json, os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
load_dotenv()
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
def subject():
    data = request.get_json()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',threaded=True)