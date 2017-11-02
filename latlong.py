# Using Python requests and the Google Maps Geocoding API.
#
# from https://gist.github.com/pnavarrc/5379521
#
# References:
#
# * http://docs.python-requests.org/en/latest/
# * https://developers.google.com/maps/

import requests

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

#This is where we wil put the string we want to get a latlong for
term = 'UMN'

params = {
    'address': term,
    'sensor': 'false',
}

# Do the request and get the response data
req = requests.get(GOOGLE_MAPS_API_URL, params=params)
res = req.json()

# Use the first result
result = res['results'][0]

geodata = dict()
geodata['lat'] = result['geometry']['location']['lat']
geodata['lng'] = result['geometry']['location']['lng']
geodata['address'] = result['formatted_address']

#print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
print('({lat}, {lng})'.format(**geodata))
# 221B Baker Street, London, Greater London NW1 6XE, UK. (lat, lng) = (51.5237038, -0.1585531)
