import requests
import humiditytester
url = 'http://50.116.54.247:3000/'

humid, temp = humiditytester.temp()

if (humid != 0 && temp != 0)  :
    obj = {'humidity' : humid,
            'temperature' : temp}
    x = requests.post(url, obj)