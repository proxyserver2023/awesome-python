import requests
from redis import Redis
from rq import Queue


def count_words_at_url(url='https://www.google.com'):
    resp = requests.get(url)
    return len(resp.text.split())
