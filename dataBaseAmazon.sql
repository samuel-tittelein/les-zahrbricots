CREATE TABLE IF NOT EXISTS USER(
    id SERIAL,
    name VARCHAR
);

CREATE TABLE IF NOT EXISTS PRODUCT(
    id SERIAL,
    name VARCHAR,
    price DECIMAL,
    category varchar
);

CREATE TABLE IF NOT EXISTS THE_PRICE_IS_RIGHT(
    id_user INTEGER,
    id_product INTEGER,
    nb_tries INTEGER,
    FOREIGN KEY (id_product) REFERENCES PRODUCT(id),
    FOREIGN KEY (id_user) REFERENCES USER(id),
    PRIMARY KEY (id_user, id_product)
);