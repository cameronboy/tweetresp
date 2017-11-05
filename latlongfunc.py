# Using Python requests and the Google Maps Geocoding API.
#
# from https://gist.github.com/pnavarrc/5379521
#
# References:
#
# * http://docs.python-requests.org/en/latest/
# * https://developers.google.com/maps/

import requests

def latlong (term):

    GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

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

    #return '({lat}, {lng})'.format(**geodata)
    return '{lat}\t{lng}'.format(**geodata)
