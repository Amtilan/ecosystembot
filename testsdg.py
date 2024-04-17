import requests
import urllib.request as urlopen
import urllib.request as request
import json 

url = "https://unstats.un.org/SDGAPI/v1/sdg/Goal/List?includechildren=true"
req = request.Request(url)
response = urlopen.urlopen(req)
response_bytes = response.read()
json_data = json.loads(response_bytes.decode("UTF-8"))

if (json_data):
    print(json_data[0])