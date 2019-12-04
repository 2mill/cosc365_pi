import requests
import humiditytester
url = 'http://50.116.54.247:3000/'

obj = {'temp' : humiditytester.temp()}
x = requests.post(url, obj)