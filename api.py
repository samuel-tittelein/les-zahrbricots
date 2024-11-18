import requests
import random
import sqlite3

from amazonBDD import getProductsCategory

def get_random_id_product(categorie):
    products = getProductsCategory(categorie)
    return random.choice(products)[0]

def get_infos(id_product):
    url = "http://ws.chez-wam.info/" + id_product
    try :
        response = requests.get(url).json()

        name = response['title'].split(',')[0]
        price = response['price']
        img = response['images'][0]
        return name, price, img
    except ValueError :
        print('id de produit non valide : ' + id_product)



##Debug
#id_product = "B07YQFZ6CJ"
#print(get_infos(id_product))

#id_product = get_random_id_product("informatique")
#print(get_infos(id_product))
