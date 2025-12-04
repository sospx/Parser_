from datetime import datetime
import requests as req
from bs4 import BeautifulSoup as BS
import hashlib


def get_soup(url):
    response = req.get(url)
    soup = BS(response.text, "lxml")
    return soup


def date_setup(data, curr, new):
    date_formating = datetime.strptime(data, curr).date().strftime(new)
    return date_formating


def hash_(object):
    hash_object = hashlib.sha256()
    hash_object.update(object.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig
