CREATE TABLE cafe(
    id INTEGER NOT NULL PRIMARY KEY,
    city VARCHAR(100)  NOT NULL,
    number VARCHAR(100)  NOT NULL,
    name VARCHAR(100)  NOT NULL,
    address VARCHAR(100)  NOT NULL,
    Menu_ID INTEGER NOT NULL,
    Staff_ID INTEGER NOT NULL,
    FOREIGN KEY (Menu_ID) REFERENCES Menu(id),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(id)
);

CREATE TABLE staff(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    Surname VARCHAR(50) NOT NULL,
    Patronymic VARCHAR(50) NOT NULL,
    date VARCHAR(50) NOT NULL,
    cafe VARCHAR(50) NOT NULL,
    Post_ID INTEGER NOT NULL,
    order_ID INTEGER NOT NULL,
    FOREIGN KEY (Post_ID) REFERENCES Post(id),
    FOREIGN KEY (order_ID) REFERENCES order(id)
);

CREATE TABLE Menu(
    id INTEGER NOT NULL PRIMARY KEY,
    price VARCHAR(100) NOT NULL,
    weight VARCHAR(100) NOT NULL,
    ingredient VARCHAR(100) NOT NULL,
    availability VARCHAR(100) NOT NULL,
    name_of_the_dish_ID INTEGER NOT NULL,
    FOREIGN KEY (name_of_the_dish_ID) REFERENCES name_of_the_dish(id)
);

CREATE TABLE name_of_the_dish(
    id INTEGER NOT NULL PRIMARY KEY,
    Dish VARCHAR(150)
);

CREATE TABLE post(
    id INTEGER NOT NULL PRIMARY KEY,
    name_post VARCHAR(150) NOT NULL
);

CREATE TABLE order(
    id INTEGER NOT NULL PRIMARY KEY,
    name_order VARCHAR(100) NOT NULL,
    Dish VARCHAR(100) NOT NULL
);

INSERT INTO cafe(city, number, name, address)
VALUES ('city', 'number', 'name', 'address'),('city1', 'number1', 'name1', 'address1');

INSERT INTO staff(name, Surname, Patronymic, date, cafe)
VALUES ('name','Surname','Patronymic','date','cafe'),('name1','Surname1','Patronymic1','date1','cafe1');

INSERT INTO menu(price, weight, ingredient, availability)
VALUES ('price','weight','ingredient','availability'),('price1','weight1','ingredient1','availability1');

INSERT INTO name_of_the_dish(Dish)
VALUES ('Dish'),('Dish1');

INSERT INTO post(name_post)
VALUES ('name_post'),('name_post1');

INSERT INTO order(name_order,Dish)
VALUES ('name_order', 'Dish'),('name_order1', 'Dish1');