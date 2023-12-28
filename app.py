from flask import Flask, render_template, request, redirect, send_from_directory, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os,json,jieba
import predict



app = Flask(__name__)


limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[],
    storage_uri="memory://",
)

'''
@app.route('/')
def home():
    return render_template('index.html')
'''

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
#@limiter.limit("1/2second", override_defaults=True)
def subject():
    RequestJson = request.get_json()
    text = RequestJson['text']
    return {'subject':predict.SubjNumTranslator(predict.MakePred(text))}

if __name__ == "__main__":
        app.run(debug=True)
