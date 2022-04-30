-- #1
-- SELECT DISTINCT
-- COUNT(product_name)
-- FROM globus; 

-- #2
-- SELECT product_name, product_amount FROM narodnii
-- GROUP BY product_id
-- HAVING day_to_expire < 2;

-- #3
-- SELECT SUM(globus.product_amount) AS Globus, SUM(narodnii.product_amount) AS Narodnii
-- FROM globus
-- INNER JOIN narodnii
-- ON globus.product_name = 'Snikers' AND narodnii.product_name = 'Snikers';

-- #4
-- SELECT globus.product_name AS Globus, narodnii.product_name AS Narodnii
-- FROM globus
-- INNER JOIN narodnii
-- ON globus.product_type_id = globus.day_to_expire
-- AND narodnii.product_type_id = narodnii.day_to_expire;

-- #5
-- SELECT 
-- globus.product_name, globus.day_to_expire AS Globus, 
-- narodnii.product_name, narodnii.day_to_expire AS Narodnii
-- FROM globus
-- INNER JOIN narodnii
-- ON globus.day_to_expire = narodnii.day_to_expire;

-- #6
-- import psycopg2
-- conn = psycopg2.connect(
--     database = 'followers',
--     user='Avtandil',
--     password='12345',
--     host='localhost',
--     port=5432
-- )
-- cur = conn.cursor()
-- cur.execute("SELECT COUNT('piyaz') FROM globus")
-- print(cur.fetchall())

-- #7
-- import psycopg2
-- conn = psycopg2.connect(
--     database = 'followers',
--     user='Avtandil',
--     password='12345',
--     host='localhost',
--     port=5432
-- )
-- cur = conn.cursor()
-- cur.execute("DELETE FROM narodnii WHERE day_to_expire < 1")
-- print(cur.fetchall())

-- #8
-- DELETE FROM globus
-- USING narodnii
-- WHERE 
-- globus.product_name = narodnii.product_name AND
-- globus.day_to_expire = narodnii.day_to_expire;

-- #9
-- SELECT * FROM narodnii
-- WHERE product_amount BETWEEN
-- 200 AND 1001;

-- #10
-- SELECT 
-- globus.date_delivered AS GLOBUS, narodnii.date_delivered AS NARODNII
-- FROM globus
-- FULL OUTER JOIN narodnii
-- ON globus.date_delivered = narodnii.date_delivered;

-- #11
-- SELECT globus.product_name
-- FROM globus
-- LEFT JOIN narodnii
-- ON globus.* = narodnii.*;

-- #12
-- SELECT narodnii.product_name
-- FROM narodnii
-- LEFT JOIN globus
-- ON narodnii.* = globus.*;

-- #13
-- SELECT globus.product_name
-- FROM globus
-- LEFT JOIN narodnii
-- ON globus.* = narodnii.*;

-- #14
-- SELECT COUNT(globus.product_name)
-- FROM globus
-- LEFT JOIN narodnii
-- ON globus.product_name = narodnii.product_name;

-- #15
-- SELECT product_name FROM globus
-- WHERE 
-- product_name LIKE '%a' OR
-- product_name LIKE '%b' OR
-- product_name LIKE '%c' OR
-- product_name LIKE '%d' OR
-- product_name LIKE '%e' OR
-- product_name LIKE '%f' OR
-- product_name LIKE '%g';

