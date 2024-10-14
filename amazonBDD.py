import sqlite3

con = sqlite3.connect('amazonBDD.db')

def createTables():
    cur = con.cursor()
    with open("mon_script.sql") as fichier:
        sql_script = fichier.read()
        fichier.close()
    cur.executescript(sql_script)
    con.commit()

def createUser(name, password):
    cur = con.cursor()
    cur.execute("INSERT INTO user (name, password) VALUES ('?', '?')", [name, password])
    con.commit()


def createProduct(name, price):
    cur = con.cursor()
    cur.execute("INSERT INTO product (name, price) VALUES ('?', '?')", [name, price])
    con.commit()

def createThePriceIsRight(id_user, id_product, nb_tries):
    cur = con.cursor()
    cur.execute("INSERT INTO product (id_user, id_product, nb_tries) VALUES ('?', '?')", [id_user, id_product, nb_tries])
    con.commit()

def getProductCategory(category):
    cur = con.cursor()
    cur.execute("SELECT * FROM ARTICLE WHERE id_category")
    con.commit()


con.close()