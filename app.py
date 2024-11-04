from flask import Flask, render_template, request
import api

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('acceuil.html', categories=["Informatique", "Musique", "Vetements"])

@app.route('/game', methods=['POST'])
def game():
    set_item()  # Set initial product data before rendering
    return render_template('index.html', name=product_name, price=product_price)

product_price = 15  # default price, to be updated from the API
product_name = "test"  # default name, to be updated from the API

def set_item():
    global product_name, product_price
    category = request.form.get('categorie')
    #id = api.get_random_id_product(category)
    id = "B076125HMB"
    product_name, product_price, img = api.get_infos(id)
    print(product_name, product_price)

@app.route('/guess', methods=['POST'])
def guess():
    global product_name, product_price
    guess_price = request.form.get('guess', '').strip()

    if not guess_price:
        return render_template('index.html', response='Merci d\'entrer un prix', name=product_name, price=product_price)
    
    guess_price = float(guess_price)

    if guess_price < product_price:
        response = f"Vous avez entrez {guess_price}€, ce qui est trop bas"
    elif guess_price > product_price:
        response = f"Vous avez entrez {guess_price}€, ce qui est trop haut"
    else:
        response = "You guessed the correct price"
        set_item()  # Reset item on correct guess

    return render_template('index.html', response=response, name=product_name, price=product_price)

if __name__ == '__main__':
    app.run(debug=True)
