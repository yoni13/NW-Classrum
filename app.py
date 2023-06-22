from flask import Flask, render_template, request, redirect, send_from_directory
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