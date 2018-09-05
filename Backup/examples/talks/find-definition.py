import requests
from urllib import urlencode


def find_definition(word):
    q = 'define ' + word
    url = 'http://api.duckduckgo.com'
    url += urlencode({'q': q, 'format':'json'});
    response = requests.get(url)
    data = response.json()
    definition = data[u'Definition']
    if definition == u'':
        raise ValueError('that is not a word');
    return definition

print find_definition('examination')
