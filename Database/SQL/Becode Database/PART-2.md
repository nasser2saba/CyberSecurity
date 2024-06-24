
# SQL Database Documentation of Part 2

This file contains the entire SQL project process documented step by step for Part 2.

## Part 2

In a second .sql file, you'll store the queries that will enable you to perform these actions:

- Display all data.
- Display first names only.
- Display first names, dates of birth and school.
- Show only female students.
- Displays only students who belong to Addy's school.
- Displays only students' first names, in reverse alphabetical order
(DESC). Next, the same thing, but limiting the results to 2.
- Adds Ginette Dalor, born 01/01/1930 and living in Brussels, still in
SQL.
- Modify Ginette (still in SQL) and change her gender and first name to "Omer".
- Delete the person whose ID is 3.
- Change the contents of the School column so that "1" is replaced by "Liege" and "2" is replaced by "Gent". (pay attention to column type!)






### Let's Start

**There's only one issue that I'm going to mention, the students.sql database is in french, while this script is in english, so make sure you translate it: 
name -> nom 
first_name -> prenome

or you could translate the students.sql file into Enflish.



1. **Create a New SQL File**: Create a file named `queries.sql` in your project directory (`~/Github/Cybersecurity/SQL/Becode Database/`).

2. **Add the SQL Queries**: Add the following SQL queries to the `queries.sql` file:

```sql
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
```

### Explanation of Each Query:

1. **Display all data**:
   ```sql
   SELECT * FROM students;
   ```

2. **Display first names only**:
   ```sql
   SELECT first_name FROM students;
   ```

3. **Display first names, dates of birth and school**:
   ```sql
   SELECT first_name, date_of_birth, school FROM students;
   ```

4. **Show only female students**:
   ```sql
   SELECT * FROM students WHERE gender = 'Female';
   ```

5. **Displays only students who belong to Addy's school**:
   ```sql
   SELECT * FROM students WHERE school = 'Addy';
   ```

6. **Displays only students' first names, in reverse alphabetical order (DESC)**:
   ```sql
   SELECT first_name FROM students ORDER BY first_name DESC;
   ```

7. **Displays only students' first names, in reverse alphabetical order (DESC), limiting the results to 2**:
   ```sql
   SELECT first_name FROM students ORDER BY first_name DESC LIMIT 2;
   ```

8. **Adds Ginette Dalor, born 01/01/1930 and living in Brussels**:
   ```sql
   INSERT INTO students (first_name, last_name, date_of_birth, city, gender, school)
   VALUES ('Ginette', 'Dalor', '1930-01-01', 'Brussels', 'Female', 'Unknown');
   ```

9. **Modify Ginette and change her gender and first name to "Omer"**:
   ```sql
   UPDATE students
   SET first_name = 'Omer', gender = 'Male'
   WHERE first_name = 'Ginette' AND last_name = 'Dalor';
   ```

10. **Delete the person whose ID is 3**:
    ```sql
    DELETE FROM students WHERE id = 3;
    ```

11. **Change the contents of the School column so that "1" is replaced by "Liege" and "2" is replaced by "Gent"**:
    ```sql
    UPDATE students
    SET school = CASE
        WHEN school = '1' THEN 'Liege'
        WHEN school = '2' THEN 'Gent'
        ELSE school
    END;
    ```

### Running the Queries

You can run these queries using the `mariadb` command-line tool:

1. **Navigate to Your Project Directory**:

    ```sh
    cd ~/Github/Cybersecurity/SQL/Becode\ Database/
    ```

2. **Run the SQL File**:

    ```sh
    mariadb -u root -p becode < queries.sql
    ```

    Enter your password when prompted.
    

By following these steps, you will be able to execute all the queries in the `queries.sql` file. 
