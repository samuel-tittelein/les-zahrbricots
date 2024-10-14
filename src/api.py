import requests
import random
import sqlite3

con = sqlite3.connect('amazonBDD.db')

def get_infos(id_product):
    url = "http://ws.chez-wam.info/" + id_product
    try :
        response = requests.get(url).json()

        name = response['title'].split(',')[0]
        price = response['price']
        img = response['images'][0]
    except ValueError :
        print('id de produit non valide : ' + id_product)

    return (name, price, img)

##Debug
#id_product = "B07YQFZ6CJ"
#print(get_infos(id_product))