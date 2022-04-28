-- #1
-- SELECT COUNT(*) FROM users;

-- #2
-- SELECT login, followers FROM users
-- WHERE followers = 
-- (SELECT MAX(followers) FROM users);

-- #3
-- SELECT * FROM users
-- WHERE followers = 
-- (SELECT MAX(followers) FROM users);

-- #4
-- SELECT AVG(followers) FROM users

-- #5
-- SELECT * FROM users
-- ORDER BY login;

-- #6
-- SELECT * FROM users
-- ORDER BY country;

-- #7
-- SELECT * FROM users
-- ORDER BY email;

-- #8
-- SELECT user_id, login FROM users;

-- #9
-- SELECT * FROM users
-- WHERE login LIKE '%as%'
-- OR login LIKE '%cg%'
-- OR login LIKE '%si%'
-- OR login LIKE '%am%'
-- OR login LIKE '%qwe%'
-- OR login LIKE '%er%'
-- OR login LIKE '%ka%'
-- OR login LIKE '%an%';

-- #10
-- SELECT * FROM users
-- WHERE login LIKE '%lol'
-- OR login LIKE '%kan'
-- OR login LIKE '%ck'
-- OR login LIKE '%ie'
-- OR login LIKE '%ig';

-- #11
-- SELECT * FROM users
-- WHERE login LIKE 'a%'
-- OR login LIKE 'b%'
-- OR login LIKE 'c%'
-- OR login LIKE 'd%'
-- OR login LIKE 'M%'
-- OR login LIKE 'D%'
-- OR login LIKE 'A%';

-- #12
-- SELECT * FROM users WHERE
-- (profession = 'Senior Programmer')
-- AND (country = 'Israel')
-- AND (followers = 
-- (SELECT MAX(followers) FROM users));

---------------------------------------

-- #1
-- SELECT * FROM users
-- WHERE email = '';

-- #2
-- SELECT COUNT(email) FROM users
-- WHERE email = '';

-- #3
-- SELECT login, phone_number FROM users
-- WHERE profession = 'Web Developer';

-- #4
-- UPDATE users
-- SET email = 'user@gmail.com'
-- WHERE email = '';

-- #5
-- SELECT login, country FROM users
-- WHERE profession = 'Unemployed';

-- #6
-- UPDATE users
-- SET phone_number = '+996705432311'
-- WHERE phone_number LIKE '%000%';

-- #7
-- DELETE FROM users
-- WHERE password IN ('12345', 'user1236', 'qwert');

-- #8
-- SELECT email FROM users
-- WHERE profession = '.NET Developer'
-- ORDER BY login;