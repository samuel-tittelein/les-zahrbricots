from unicodedata import category

from amazonBDD import *
from api import id_product, get_infos
from csv_parser import read_csv

def fill_product(file_path):
    createTables()

    values = read_csv(file_path)

    for product in values:
        id_product = product[0]
        name, price, img = get_infos(id_product)
        category = product[1]

        createProduct(name, price, category)
