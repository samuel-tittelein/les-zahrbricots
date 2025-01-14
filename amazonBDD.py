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

def createUser(name):
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO user (name) VALUES (?)", (name,))
        con.commit()
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()

def createProduct(id, category):
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO product (id, category) VALUES (?, ?)", [id, category])
        con.commit()
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()


def createThePriceIsRight(id_user, id_product, product_price, nb_tries):
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        print("price is right", id_user, id_product, product_price, nb_tries)
        cur.execute("INSERT INTO THE_PRICE_IS_RIGHT (id_user, id_product, price, nb_tries) VALUES (?, ?, ?, ?)", [id_user, id_product, product_price, nb_tries])
        con.commit()
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()

#renvoie tous les produits en fonction d'un tableau de categorie'
def getProductsCategory(category):
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM PRODUCT WHERE category = ?", (category,))
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
        cur.execute("SELECT DISTINCT(category) FROM PRODUCT")
        categories = cur.fetchall()
        return categories
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()

def get_name(id_user):
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        cur.execute("SELECT name FROM USER WHERE id =?", (id_user,))
        name = cur.fetchone()
        return name[0]
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()

def get_category(id_product):
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        cur.execute("SELECT category FROM PRODUCT WHERE id =?", (id_product,))
        category = cur.fetchone()
        return category[0]
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()

def get_user_id(name):
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        cur.execute("SELECT id FROM USER WHERE name =?", (name,))
        id_user = cur.fetchone()
        return id_user[0]
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()

#récupérer le podium
def getPodium(category):
    con = sqlite3.connect('dataBase.db')
    cur = con.cursor()
    try:
        print('pod : ', "(\'" + category + "\',)")
        print('cat : ', getCategories())
        cur.execute("SELECT USER.name, nb_tries, price FROM THE_PRICE_IS_RIGHT INNER JOIN USER ON THE_PRICE_IS_RIGHT.id_user = USER.id INNER JOIN PRODUCT ON PRODUCT.id = THE_PRICE_IS_RIGHT.id_product WHERE PRODUCT.category =? ORDER BY nb_tries LIMIT 5", (category,))
        podium = cur.fetchall()
        print('pod : ', podium)
        return podium
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()


