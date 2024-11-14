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
        category = product[1]
        createProduct(id_product, category)
