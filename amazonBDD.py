import sqlite3

def createTables():
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        with open("dataBaseAmazon.sql") as fichier:
            sql_script = fichier.read()
            fichier.close()
        cur.executescript(sql_script)
        con.commit()
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()

def createUser(name, password):
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO user (name, password) VALUES ('?', '?')", [name, password])
        con.commit()
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()

def createProduct(name, price):
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO product (name, price) VALUES ('?', '?')", [name, price])
        con.commit()
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()


def createThePriceIsRight(id_user, id_product, nb_tries):
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO product (id_user, id_product, nb_tries) VALUES ('?', '?')", [id_user, id_product, nb_tries])
        con.commit()
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()

#renvoie tous les produits en fonction d'un tableau de categorie'
def getProductsCategory(categories):
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM ARTICLE WHERE id_category in ?", categories)
        products = cur.fetchall()
        return products
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()

#renvoie tous les categories
def getCategories():
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        cur.execute("SELECT DISTINCT(category) FROM ARTICLE")
        categories = cur.fetchall()
        return categories
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()

