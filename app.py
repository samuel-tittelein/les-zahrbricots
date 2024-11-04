from flask import Flask, render_template, request
import amazonBDD
import api

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('acceuil.html', categories=["Informatique","Musique","Vetements"]) #A modifier

@app.route('/game', methods=['POST'])
def game():
    #name = request.form['username']
    #amazonBDD.createUser(name,password)
    set_item()
    return render_template('index.html')

price = 15 #prix du produit /!\ a recuperer de la base de donnees
name = "test" #nom du produit /!\ a recuperer de la base de donnees

def set_item():
    global name,price
    id_product = api.get_random_id_product("Informatique")
    name, price, img = api.get_infos(id_product)



@app.route('/guess', methods=['POST'])
def guess():
    guess_price = request.form['guess']
    if guess_price == '':
        return render_template('index.html', response='Merci d\'entrer un prix',name=name)
    else:
        guess_price = float(guess_price)
        #A modifier ça fait trop de return
        if guess_price < price:
            return render_template('index.html', response="Vous avez entrez " + str(guess_price) + "$ ce qui est trop bas",name=name)
        elif guess_price > price:
            return render_template('index.html', response="Vous avez entrez " + str(guess_price) + "$ ce qui est trop haut",name=name)
        else:
            #Le prix est bon faut changer l'item
            return render_template('index.html', response="You guessed the correct price",name=name0)


if __name__ == '__main__':
    app.run(debug=True)