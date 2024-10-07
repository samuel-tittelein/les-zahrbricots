import requests

url = "http://ws.chez-wam.info/"

#TODO retourner un id de produit random
id_product = None
url += id_product

response = requests.get(url)

img = response['images'][0]
price = response['price']
name = response['title'].split(',')[0]