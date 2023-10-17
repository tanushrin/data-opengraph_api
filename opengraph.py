# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    """
    Return a dictionary of OpenGraph metadata found in HTML of given url
    """
    dict1 = {}
    url_name = url
    response = requests.get(f"https://opengraph.lewagon.com/?url={url_name}")
    if response.status_code != 200:
        return dict1
    #return response.json()
    return response.json()["data"]
    #pass

# To manually test, please uncomment the following lines and run `python
# opengraph.py`:
#import pprint
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(fetch_metadata("https://www.github.com"))
