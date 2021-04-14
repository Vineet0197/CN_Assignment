import flask
import json
import requests
import socket
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/postUser', methods=['POST', 'GET'])
def postUser():
    File = open('resources/Payload.json')
    json_input = File.read()
    request_json = json.loads(json_input)
    url = 'https://reqres.in/api/users'
    response = requests.post(url, request_json)
    return response.json()

hostName = socket.gethostname()
app.run(host=socket.gethostbyname(hostName), port=8090)
