from flask import Flask, render_template, request
import amazonBDD

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('acceuil.html')

@app.route('/game', methods=['POST'])
def game():
    #name = request.form['username']
    #amazonBDD.createUser(name,password)
    print("test")
    return render_template('index.html')

price = 15 #prix du produit /!\ a recuperer de la base de donnees

@app.route('/guess', methods=['POST'])
def guess():
    guess_price = request.form['guess']
    if guess_price == '':
        return render_template('index.html', response='Please enter a price')
    else:
        guess_price = float(guess_price)
        print(guess_price)
        if guess_price < price:
            return render_template('index.html', response="You guessed " + str(guess_price) + " which is too low")
        elif guess_price > price:
            return render_template('index.html', response="You guessed " + str(guess_price) + " which is too high")
        else:
            return render_template('index.html', response="You guessed the correct price")


if __name__ == '__main__':
    app.run(debug=True)