from argparse import ArgumentError

import requests
from unicodedata import category

from amazonBDD import *
from api import get_infos
from csv_parser import read_csv

def fill_product(file_path):
    createTables()
    print("Tables crées")

    values = read_csv(file_path)

    for product in values:
        id_product = product[0]
        if check_id(id_product):
            continue
        category = product[1]
        createProduct(id_product, category)

def check_id(id_product):
    url = "http://ws.chez-wam.info/" + id_product
    try :
        response = requests.get(url).json();
        name = response['title'].split(',')[0]
        price = response['price']
        img = response['images'][0]
    except :
        return False
    if name is None or price is None or img is None:
        return False
    return True

