

-- Display all data
SELECT * FROM students;

-- Display first names only
SELECT first_name FROM students;

-- Display first names, dates of birth and school
SELECT first_name, date_of_birth, school FROM students;

-- Show only female students
SELECT * FROM students WHERE gender = 'Female';

-- Display only students who belong to Addy's school
SELECT * FROM students WHERE school = 'Addy';

-- Display only students' first names, in reverse alphabetical order (DESC)
SELECT first_name FROM students ORDER BY first_name DESC;

-- Display only students' first names, in reverse alphabetical order (DESC), limiting the results to 2
SELECT first_name FROM students ORDER BY first_name DESC LIMIT 2;

-- Add Ginette Dalor, born 01/01/1930 and living in Brussels
INSERT INTO students (first_name, last_name, date_of_birth, city, gender, school)
VALUES ('Ginette', 'Dalor', '1930-01-01', 'Brussels', 'Female', 'Unknown');

-- Modify Ginette and change her gender and first name to "Omer"
UPDATE students
SET first_name = 'Omer', gender = 'Male'
WHERE first_name = 'Ginette' AND last_name = 'Dalor';

-- Delete the person whose ID is 3
DELETE FROM students WHERE id = 3;

-- Change the contents of the School column so that "1" is replaced by "Liege" and "2" is replaced by "Gent"
UPDATE students
SET school = CASE
    WHEN school = '1' THEN 'Liege'
    WHEN school = '2' THEN 'Gent'
    ELSE school
END;
