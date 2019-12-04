from flask import Flask
import humidity
app = Flask(__name__)
@app.route('/')
def main() :
    return "Welcome to my flask page" + " current temp is " + humidity.returnTemperature()
