-- #1
-- SELECT name, dp_language, sp_language FROM students; 

-- #2
-- SELECT * FROM students WHERE age > 30;

-- #3
-- SELECT * FROM students 
-- WHERE dp_language IN ('Python', 'C#')
-- OR sp_language IN  ('Python', 'C#');

-- #4
-- SELECT * FROM students 
-- WHERE 
-- (dp_language = 'Python' and 
-- sp_language = 'C#')
-- or 
-- (dp_language = 'C#' and 
-- sp_language = 'Java')

-- #5
-- DELETE FROM students 
-- WHERE id IN (1,3,5,7);

-- #6
-- SELECT * 
-- FROM students
-- WHERE age = (SELECT MIN(age) FROM students) AND 
-- (dp_language = 'Java' OR
-- sp_language = 'Java');

-- #7
-- DROP TABLE students;

-- #8
-- DROP DATABASE programmers;