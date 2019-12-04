from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello() :
    name = request.args.get("Name", "World")
    return 'Hello World'