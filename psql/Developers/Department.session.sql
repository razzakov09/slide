-- #1
-- ALTER TABLE developers
-- RENAME COLUMN skill TO age;

-- #2
-- INSERT INTO developers(
--     name,
--     age,
--     programming_lang
-- ) VALUES 
-- ('Bakyt', 23, 'Python'),
-- ('Beka', 15, 'Java'),
-- ('Gulya', 30, 'JavaScript'),
-- ('Beka', 30, 'Assembler');

-- #3
-- ALTER TABLE developers ADD COLUMN cash VARCHAR;

-- #4
-- INSERT INTO developers(
--     name,
--     age,
--     programming_lang,
--     cash
-- ) VALUES ('Katya', 16, 'Python', '3000');

-- #5
-- UPDATE developers
-- SET age = '27'
-- WHERE age > '25';

-- #6
-- COMMENT ON COLUMN developers.name IS 'Имя пользователя';

-- #7
-- UPDATE developers
-- SET name = 'Ecaterina'
-- WHERE name = 'Katya';