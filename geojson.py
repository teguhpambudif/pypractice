import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location:')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    # handling the url
    uh = urllib.request.urlopen(url)
    # pull the entire document with read method and decode it cuz it possibly an utf-8 or whatever type of data google gives us
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure to retrieve ====')
        print(data)
        continue

    lat = js["result"][0]["geometry"]["location"]["lat"]
    lng = js["result"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['result'][0]['formatted_address']
    print(location)