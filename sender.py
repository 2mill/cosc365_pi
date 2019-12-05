import requests
import time
from datetime import datetime 
import humiditytester
url = 'http://50.116.54.247:3000/'

humid = 0
temp = 0
obj = 0
while True :
    print("10 seconds have passed")
    obj = {'humidity' : humiditytester.humidity(),
        'temperature' :humiditytester.temp(),
        'currentDate' : datetime.now()}
        
    x = requests.post(url, obj)
    time.sleep(10);