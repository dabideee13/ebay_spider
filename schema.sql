CREATE TABLE product_data (
    id serial PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    url TEXT NOT NULL,
    price VARCHAR(200) NOT NULL,
    image_url TEXT NOT NULL
);
