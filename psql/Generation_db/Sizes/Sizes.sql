-- #1
-- CREATE TABLE sizes(
-- id SERIAL PRIMARY KEY,
-- size_of_leg INTEGER,
-- time_of_creating VARCHAR);

-- INSERT INTO sizes(
--     size_of_leg,
--     time_of_creating
-- ) VALUES
-- (44, '22.02.2022'),
-- (34, '12.05.2012'),
-- (24, '2.05.3012')

-- #2
-- CREATE TABLE man(
-- size_id integer REFERENCES sizes(id),
-- name VARCHAR);

-- INSERT INTO man(
--     size_id,
--     name
-- ) VALUES
-- (1, 'Avtandil'),
-- (2, 'Oleg'),
-- (3, 'Sasha')

-- SELECT man.name, sizes.size_of_leg
-- FROM man
-- INNER JOIN sizes
-- ON sizes.id = man.size_id;

