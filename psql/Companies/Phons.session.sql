-- #1
-- createdb companies;

-- #2
-- CREATE TABLE phons(
-- id SERIAL PRIMARY KEY,
-- name VARCHAR,
-- price INTEGER);

-- #3
-- INSERT INTO phons(
--     name,
--     price
-- ) VALUES ('Iphone', 1000);

-- #4
-- ALTER TABLE phons ADD COLUMN country VARCHAR;

-- #5, #6, #7, #8
-- INSERT INTO phons(
--     name,
--     price,
--     country
-- ) VALUES 
-- ('Samsung', 800, 'Korea'),
-- ('Nokia', 200, 'Kyrgyzstan'),
-- ('MI', 1, 'Uzbekistan'),
-- ('GOOGLE', 0, 'USA');

-- #9
-- CREATE TABLE cars(
-- id SERIAL PRIMARY KEY,
-- name VARCHAR,
-- price INTEGER DEFAULT 300);

-- #10
-- INSERT INTO cars(
--     name,
--     price
-- ) VALUES ('MB', 1000);

-- #11
-- ALTER TABLE cars ADD COLUMN country VARCHAR;

-- #12, #13, #14
-- INSERT INTO cars(
--     name,
--     price,
--     country
-- ) VALUES 
-- ('Audi', 300, 'Germany'),
-- ('BMW', 11800, 'Germany'),
-- ('Tulpar', 1111800, 'Kyrgzstan');

-- #15
-- UPDATE cars
-- SET country = 'Germany'
-- WHERE name = 'MB';

-- #16
-- DELETE FROM cars
-- WHERE price < 1000;
