from unicodedata import category

from flask import Flask, render_template, request, redirect, url_for
import api
from amazonBDD import getCategories, getPodium, createThePriceIsRight, get_category, createUser
from fill_db import fill_product

app = Flask(__name__)

@app.route('/')
def home():
    categories = getCategories()
    for i in range(len(categories)):
        categories[i] = categories[i][0]
    return render_template('accueil.html', categories = categories)

id_product = "" # default id
product_price = 15  # default price, to be updated from the API
product_name = "test"  # default name, to be updated from the API
product_image = "test"  # default image, to be updated from the API
username = "" # default username, to be updated from the user
nb_tries = 0 # default number of tries

@app.route('/game', methods=['POST'])
def game():
    global username
    username = request.form.get('username')
    createUser(username)
    set_item()  # Set initial product data before rendering
    return render_template('index.html', name=product_name, price=product_price)

def set_item():
    global id_product, product_name, product_price, product_image
    category = request.form.get('categorie')
    id_product = api.get_random_id_product(category)
    try:
        product_name, product_price, product_image = api.get_infos(id_product)
        product_price = product_price.replace("€", "")
        product_price = product_price.replace(",", ".")
    except:
        set_item()
    print(product_name, product_price)

@app.route('/guess', methods=['POST'])
def guess():
    global id_product, product_name, product_price, product_image, username, nb_tries
    guess_price = request.form.get('guess', '').strip()
    nb_tries = 0

    if not guess_price:
        return render_template('index.html', response='Merci d\'entrer un prix', name=product_name, price=product_price, image=product_image)
    
    guess_price = float(guess_price)

    product_price = float(product_price)
    nb_tries += 1

    if guess_price < product_price:
        response = f"Vous avez entrez {guess_price}€, ce qui est trop bas"
    elif guess_price > product_price:
        response = f"Vous avez entrez {guess_price}€, ce qui est trop haut"
    else:
        createThePriceIsRight(username, id_product, nb_tries)
        return redirect(url_for('podium', nb_tries=nb_tries))
    return render_template('index.html', response=response, name=product_name, price=product_price, image=product_image)

@app.route('/podium', methods=['GET'])
def podium():
    global username, id_product
    nb_tries = request.args.get('nb_tries')  # Récupère le paramètre 'category'
    category = get_category(id_product)
    podium = getPodium(category)
    print('podium : ', podium)
    return render_template('podium.html', podium=podium, category=category, nb_tries=nb_tries)


if __name__ == '__main__':
    fill_product('Categories.csv')
    app.run(debug=True)
