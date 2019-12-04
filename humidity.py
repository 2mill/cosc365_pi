import Adafruit_DHT
from flask import Flask, escape, request


DHT_SENSOR = Adafruit_DHT.DHT22

DHT_PIN = 4


@app.rout('/')
def hello() :
    # while True :
      humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
      if humidity is not None and temperature is not None:
          ("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))
      else :
          print("Failed to retrieve data from humidity sensor")
# from flask import Flask, escape, request

# app = Flask(__name__)

# @app.route('/')
# def hello() :
#     name = request.args.get("Name", "World")
#     return 'Hello World'