DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS re_sell;
DROP TABLE IF EXISTS buy_details;
DROP TABLE IF EXISTS re_buy_rent;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS re_obj;
DROP TABLE IF EXISTS re_types;
DROP TABLE IF EXISTS buyers;
DROP TABLE IF EXISTS sellers;
DROP TABLE IF EXISTS users;


CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    login TEXT,
    password_hash TEXT,
    password_salt TEXT,
    username VARCHAR(64)
);

CREATE TABLE sellers (
    seller_id INT PRIMARY KEY,
    seller_name TEXT,
    email TEXT,
    phone TEXT,
    info TEXT,
    photo TEXT,
    type VARCHAR(64),
    FOREIGN KEY (seller_id) REFERENCES users (user_id)
);

CREATE TABLE buyers (
    buyer_id INT PRIMARY KEY,
    buyer_name TEXT,
    email TEXT,
    phone TEXT,
    info TEXT,
    photo TEXT,
    type VARCHAR(64),
    FOREIGN KEY (buyer_id) REFERENCES users (user_id)
);

CREATE TABLE re_types (
    type_id SERIAL PRIMARY KEY,
    type VARCHAR(64)
);

CREATE TABLE re_obj (
    re_id SERIAL PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    info TEXT,
    type_id INT,
    post_date TIMESTAMP,
    exp_date TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES re_types (type_id)
);

CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY,
    country VARCHAR(64),
    state VARCHAR(64),
    city VARCHAR(64),
    district VARCHAR(64)
);

CREATE TABLE re_buy_rent (
    user_id INT,
    buy_rent_id INT PRIMARY KEY,
    price_min INT,
    price_max INT,
    check_in VARCHAR(16),
    check_out VARCHAR(16),
    FOREIGN KEY (buy_rent_id) REFERENCES re_obj (re_id),
    FOREIGN KEY (user_id) REFERENCES buyers (buyer_id)
);

CREATE TABLE buy_details(
    buy_id INT PRIMARY KEY,
    location_id INT,
    FOREIGN KEY (buy_id) REFERENCES re_buy_rent (buy_rent_id),
    FOREIGN KEY (location_id) REFERENCES locations (location_id)
);

CREATE TABLE re_sell (
    user_id INT,
    re_sell_ID INT PRIMARY KEY,
    price INT,
    location_id INT,
    FOREIGN KEY (re_sell_id) REFERENCES re_obj (re_id),
    FOREIGN KEY (user_id) REFERENCES sellers (seller_id),
    FOREIGN KEY (location_id) REFERENCES locations (location_id)
);

CREATE TABLE comments (
    comment_id SERIAL PRIMARY KEY,
    comment_from_id INT,
    comment_to_id INT,
    title VARCHAR(64),
    content TEXT,
    date TIMESTAMP,
    FOREIGN KEY (comment_from_id) REFERENCES users (user_id),
    FOREIGN KEY (comment_to_id) REFERENCES users (user_id)
)
