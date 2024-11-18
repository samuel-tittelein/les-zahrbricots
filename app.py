from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import api
from amazonBDD import getCategories, getPodium, createThePriceIsRight, get_category, createUser, get_user_id
from fill_db import fill_product, add_product
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(24)  # This key is stored inside the .env file as FLASK_SECRET_KEY

@app.route('/')
def home():
    categories = getCategories()
    for i in range(len(categories)):
        categories[i] = categories[i][0]
    return render_template('accueil.html', categories = categories)

@app.route('/game', methods=['POST'])
def game():
    username = request.form.get('username')
    category = request.form.get('categorie')
    if not category:
        category = session.get('category')
    
    # Store user and game data in the session
    # The session is stored inside the browser's cookies
    session['username'] = username
    session['category'] = category
    session['nb_tries'] = 0
    
    createUser(username)
    print()
    return render_template('index.html')

@app.route('/nouveau', methods=['GET', 'POST'])
def nouveau():
    if request.method == 'GET':
        return render_template('nouvel_item.html')
    if request.method == 'POST':
        name = request.form.get('itemId', '').strip()
        category = request.form.get('category', '').strip()
        add_product(name, category)
        return redirect('/')


def set_item(category):
    while True:
        id_product = api.get_random_id_product(category)
        try:
            name, price, image = api.get_infos(id_product)
            if price.strip() == "":
                continue 

            price = price.replace("€", "").replace(",", ".")
            price = float(price)  # Convert price to a numeric type

            return {'id': id_product, 'name': name, 'price': price, 'image': image}
        except Exception:
            continue  # Retry on failure


@app.route('/api/set_item', methods=['POST'])
def api_set_item():
    category = session['category']
    if not category:
        return jsonify({'error': 'Category is required'}), 400

    product_data = set_item(category)
    session['product'] = product_data

    return jsonify(product_data)

@app.route('/guess', methods=['POST'])
def guess():
    guess_price = request.form.get('guess', '').strip()
    product_data = session.get('product')
    username = session.get('username')
    nb_tries = session.get('nb_tries', 0)

    if not guess_price:
        return render_template('index.html', response='Merci d\'entrer un prix', name=product_data['name'], price=product_data['price'], image=product_data['image'])    
    try:
        guess_price = float(guess_price)
        nb_tries += 1
        session['nb_tries'] = nb_tries

        if guess_price < product_data['price']:
            response = f"Vous avez entrez {guess_price}€, ce qui est trop bas"
        elif guess_price > product_data['price']:
            response = f"Vous avez entrez {guess_price}€, ce qui est trop haut"
        else:
            userId = get_user_id(username)
            createThePriceIsRight(userId, product_data['id'], product_data['price'], nb_tries)
            return redirect(url_for('podium', nb_tries=nb_tries))

    except ValueError:
        response = "Merci d'entrer un prix valide"

    return render_template('index.html', response=response, name=product_data['name'], price=product_data['price'], image=product_data['image'])


@app.route('/podium', methods=['GET'])
def podium():
    nb_tries = session.get('nb_tries', 0)
    product_data = session.get('product')
    username = session.get('username')

    if not product_data:
        category = "informatique"
    else:
        category = get_category(product_data['id'])

    podium = getPodium(category)
    print('podium:', podium)
    
    return render_template('podium.html', podium=podium, category=category, nb_tries=nb_tries, username=username)


if __name__ == '__main__':
    fill_product('Categories.csv')
    app.run(debug=True)
