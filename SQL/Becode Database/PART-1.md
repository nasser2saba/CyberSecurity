
# SQL Database Documentation of Part 1

This file contains the entire SQL project process documented step by step for Part 1.

## Part 1

- Create a `becode` database.
- Import the `students.sql` file.

## Content: 


- [Install MySQL (MariaDB)](#step-1-install-mysql-mariadb)
- [Create the Database](#step-2-create-the-database)
- [Set Up Your Development Environment](#step-3-set-up-your-development-environment) 
- [Create the BeCode Database](#step-4-create-the-becode-database)
- [Importing the SQL file using Script](#step-6-importing-the-sql-file-using-script)
- [Results](#results)
- [Extra](#step-5-import-the-studentssql-file)


Setting up SQL on Arch Linux from scratch. We'll use MySQL (MariaDB).

#### Step 1: Install MySQL (MariaDB)

1. **Update Your Package Database**

   Open your terminal and update your package database:

   ```sh
   sudo pacman -Syu
   ```

2. **Install MariaDB**

   Install MariaDB, which is a drop-in replacement for MySQL:

   ```sh
   sudo pacman -S mariadb
   ```

3. **Initialize the MariaDB Data Directory**

   After installing, you need to initialize the data directory:

   ```sh
   sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
   ```

4. **Start and Enable the MariaDB Service**

   Start the MariaDB service and enable it to start on boot:

   ```sh
   sudo systemctl start mariadb
   sudo systemctl enable mariadb
   ```

5. **Run the Secure Installation Script**

   Run the secure installation script to set the root password and secure your database server:

   ```sh
   sudo mysql_secure_installation
   ```

   Follow the prompts to set the root password and secure your installation.

   I already has a root password so i didn't change the settings, since this is also only for educational purposes and this project won't be really used irl.

#### Step 2: Create the Database

1. **Log in to MariaDB as Root**

   Log in to MariaDB using the root user:

   ```sh
   sudo mysql -u root -p
   ```

   Enter the root password you set during the secure installation.

2. **Create the "becode" Database**

   Once logged in, create the database:

   ```sql
   CREATE DATABASE becode;
   ```

  (You can also create tables if you like:)

   ```sql
   USE becode;

   CREATE TABLE students (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100),
       age INT,
       grade VARCHAR(10)
   );
   ```

#### Step 3: Set Up Your Development Environment

You can work with SQL in several ways. Here are a few recommendations:

1. **Terminal**: You can manage your databases and run SQL commands directly in the terminal using the `mysql` client. Which is what I'll be using but I added alternatives. 

2. **VSCode**: You can use Visual Studio Code with extensions for MySQL to interact with your database. Here’s how:

   - **Install VSCode**:

     If you haven't installed VSCode yet, you can install it from the AUR:

     ```sh
     sudo pacman -S code
     ```

   - **Install MySQL Extension**:

     Open VSCode and install the "SQLTools" extension from the Extensions Marketplace. It supports MySQL and provides a graphical interface to interact with your database.

   - **Configure the Extension**:

     After installing the extension, configure it to connect to your MariaDB database by adding a new connection in the SQLTools extension.


        To configure the SQLTools extension in Visual Studio Code (VSCode) to connect to your MariaDB database, follow these steps:

        1. **Install SQLTools Extension in VSCode**:
        - Open VSCode.
        - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
        - Search for `SQLTools` and install the extension.

        2. **Install SQLTools MySQL/MariaDB Driver**:
        - After installing SQLTools, you need to install the MySQL/MariaDB driver.
        - Go to the Extensions view again.
        - Search for `SQLTools MySQL/MariaDB` and install the driver.

        3. **Open SQLTools**:
        - Once the extension and driver are installed, you will see a new SQLTools icon in the Activity Bar.
        - Click on the SQLTools icon to open the SQLTools panel.

        4. **Add a New Connection**:
        - In the SQLTools panel, click on the `+` button or `Add New Connection`.
        - A new tab will open to configure your connection settings.

        5. **Configure the Connection**:
        - Fill in the connection details for your MariaDB server. Here is an example configuration:
            - **Connection Name**: `MariaDB Local`
            - **Client**: `MySQL/MariaDB`
            - **Server**: `localhost`
            - **Port**: `3306`
            - **User**: `root`
            - **Password**: `your_password`
            - **Database**: `becode`
            - **Driver Options**: You can leave these as default unless you have specific configurations.
        
        Here's a screenshot of the settings for clarity:

        ```
        {
            "name": "MariaDB Local",
            "client": "MySQL/MariaDB",
            "connection": {
            "server": "localhost",
            "port": 3306,
            "user": "root",
            "password": "your_password",
            "database": "becode"
            }
        }
        ```

        6. **Save the Connection**:
        - After filling in the details, click on the `Save` button.

        7. **Connect to the Database**:
        - You should now see the new connection listed in the SQLTools panel.
        - Click on the connection name (e.g., `MariaDB Local`) to connect to your MariaDB database.
        - You will see a new SQL Editor tab open where you can start writing and executing SQL queries.

        **Using the SQLTools Extension

        - **Running Queries**: Write your SQL queries in the SQL editor and press `Ctrl+Enter` to execute the query.
        - **Viewing Results**: The results of your queries will appear in the Results panel at the bottom of the editor.
        - **Managing Connections**: You can manage your connections (add, edit, delete) from the SQLTools panel.

        **Example Query

        Here’s how you might use the SQLTools extension to interact with your `becode` database:

        ```sql
        -- Create a new table
        CREATE TABLE IF NOT EXISTS courses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT
        );

        -- Insert data into the table
        INSERT INTO courses (name, description) VALUES ('Python Basics', 'Introduction to Python');

        -- Query the data
        SELECT * FROM courses;
        ```

        Write the above queries in the SQL editor and execute them to interact with your database.

        This should get you started with managing your MariaDB database directly from VSCode using the SQLTools extension.


3. **SQL App**: You can use database management applications like DBeaver, which is available in the AUR and provides a graphical interface to manage your databases.

   - **Install DBeaver**:

     ```sh
     sudo pacman -S dbeaver
     ```

   - **Connect to MariaDB**:

     Open DBeaver, create a new connection, and provide the necessary details to connect to your MariaDB server.

     I didn't do this because I wasn't in the mood but I've added it incase you're in the mood.



#### Step 4 Create the `becode` Database

1. **Log in to MariaDB**

   Open your terminal and log in to MariaDB as the root user:

   ```sh
   sudo mysql -u root -p
   ```

   Enter the root password you set during the secure installation.

2. **Create the Database**

   Once logged in, create the `becode` database:

   ```sql
   CREATE DATABASE becode;
   ```

3. **Exit MariaDB**

   Exit the MariaDB client:

   ```sql
   EXIT;
   ```

#### Step 5: Import the `students.sql` File

1. **Navigate to Your Project Directory**

   Change to your project directory where the `students.sql` file is located:

   ```sh
   cd ~/Github/Cybersecurity/SQL/Becode\ Database/
   ```

2. **Import the SQL File**

   Use the `mysql` client to import the `students.sql` file into the `becode` database:

   ```sh
   mysql -u root -p becode < students.sql
   ```

   Enter the root password when prompted.

   I got errors here, ended up deleting the database and restarting and then it worked.

##### Verifying the Import

To verify that the `students.sql` file was imported correctly:

1. **Log in to MariaDB**

   ```sh
   sudo mysql -u root -p
   ```

   Enter the root password.

2. **Select the `becode` Database**

   ```sql
   USE becode;
   ```

3. **List the Tables**

   List the tables to verify that the import was successful:

   ```sql
   SHOW TABLES;
   ```

4. **Query the Data**

   Query the data in one of the tables to ensure it was imported correctly:

   ```sql
   SELECT * FROM students;
   ```

   If it opens a list with names yk it worked.

5. **Exit MariaDB**

   ```sql
   EXIT;
   ```

##### Summary

- Install and set up MariaDB on Arch Linux.
- Created the `becode` database.
- Imported the `students.sql` file into the `becode` database.
- Verified the import by listing tables and querying data.




#### Step 6: Importing the SQL file using Script 

You can automate the process of creating the database, importing the SQL file, and keeping everything organized within your project directory.

1. **Create a Shell Script**: This script will handle the creation of the database, dropping it if it exists, and importing the SQL file.

2. **Run the Shell Script**: Execute the shell script from your project directory.

##### Step-by-Step Guide

###### Step 1: Create the Shell Script

1. **Open a text editor** (e.g., VS Code, nano, vim) and create a new file named `setup_db.sh` in your project directory (`~/Github/Cybersecurity/SQL/Becode Database/`).

2. **Add the following content to the script**:

    ```sh
    #!/bin/bash

    # Database credentials
    USER="root"
    PASSWORD="your_password"
    DATABASE="becode"

    # SQL file
    SQL_FILE="students.sql"

    # Check if the SQL file exists
    if [ ! -f "$SQL_FILE" ]; then
        echo "SQL file '$SQL_FILE' not found!"
        exit 1
    fi

    # Log in to MariaDB and drop the database if it exists, then create a new one
    mariadb -u $USER -p$PASSWORD -e "DROP DATABASE IF EXISTS $DATABASE; CREATE DATABASE $DATABASE;"

    # Check if the database was created successfully
    if [ $? -ne 0 ]; then
        echo "Failed to create the database '$DATABASE'."
        exit 1
    fi

    # Import the SQL file into the database
    mariadb -u $USER -p$PASSWORD $DATABASE < $SQL_FILE

    # Check if the import was successful
    if [ $? -ne 0 ]; then
        echo "Failed to import '$SQL_FILE' into the database '$DATABASE'."
        exit 1
    fi

    echo "Database '$DATABASE' setup successfully with '$SQL_FILE'."
    ```

    Replace `your_password` with your actual MariaDB root password.

3. **Save and close the file**.

###### Step 2: Make the Shell Script Executable

1. Open a terminal and navigate to your project directory:

    ```sh
    cd ~/Github/Cybersecurity/SQL/Becode\ Database/
    ```

2. Make the shell script executable:

    ```sh
    chmod +x setup_db.sh
    ```

###### Step 3: Run the Shell Script

1. Run the shell script to set up your database and import the SQL file:

    ```sh
    ./setup_db.sh
    ```

    You should see output indicating whether each step was successful.

##### Explanation

- The shell script logs into MariaDB and drops the existing `becode` database if it exists.
- It then creates a new `becode` database.
- The script checks if the SQL file `students.sql` exists in the same directory and imports it into the `becode` database.
- The script provides feedback on whether each step was successful or if there were any errors.

##### Verifying the Setup

After running the shell script, you can verify that the database and tables were created successfully by logging into MariaDB and querying the database:

1. **Log in to MariaDB**:

    ```sh
    sudo mariadb -u root -p
    ```

2. **Select the `becode` Database**:

    ```sql
    USE becode;
    ```

3. **List the Tables**:

    ```sql
    SHOW TABLES;
    ```

4. **Query the Data**:

    ```sql
    SELECT * FROM students;
    ```

By following these steps, you can automate the process of setting up your database and ensure everything is organized within your project directory. Let me know if you encounter any issues or have further questions!


#### Results

MariaDB [becode]> SHOW TABLES;
+------------------+
| Tables_in_becode |
+------------------+
| school           |
| students         |
+------------------+
2 rows in set (0.001 sec)

MariaDB [becode]> SELECT * FROM students;
+-----------+-------------+---------+---------------+-------+--------+
| idStudent | nom         | prenom  | datenaissance | genre | school |
+-----------+-------------+---------+---------------+-------+--------+
|         1 | Ere         | Molly   | 1990-11-17    | F     |      2 |
|         2 | Gavel       | Aude    | 1991-08-28    | F     |      2 |
|         3 | Cover       | Harris  | 1977-09-05    | M     |      2 |
|         4 | Nett        | Marion  | 1984-05-29    | F     |      2 |
|         5 | Ochon       | Paul    | 1994-10-09    | M     |      2 |
|         6 | Laybrise    | Sam     | 1985-07-30    | M     |      2 |
|         7 | Sion        | Eddy    | 1993-10-18    | M     |      2 |
|         8 | Beau        | Harry   | 1992-03-01    | M     |      2 |
|         9 | Touille     | Sasha   | 1978-05-16    | M     |      2 |
|        10 | Terrieur    | Alain   | 1988-11-22    | M     |      2 |
|        11 | Tarr        | Guy     | 1972-01-27    | M     |      2 |
|        12 | Door        | Théo    | 1984-06-24    | M     |      2 |
|        13 | Selayr      | Jacques | 2017-04-24    | M     |      2 |
|        14 | Karena      | Emma    | 1982-03-30    | F     |      2 |
|        15 | Egée        | Yves    | 1989-05-31    | M     |      2 |
|        16 | Tramp       | Pauline | 1980-01-03    | F     |      1 |
|        17 | Ciné        | Emma    | 1981-08-25    | F     |      1 |
|        18 | Daydui      | Jean    | 1996-05-09    | M     |      1 |
|        19 | Jean        | Serge   | 1989-07-21    | M     |      1 |
|        20 | Addy        | Jack    | 1993-04-07    | M     |      1 |
|        21 | Age         | karl    | 1991-01-25    | M     |      1 |
|        22 | Fini        | Alain   | 1993-10-03    | M     |      1 |
|        23 | Lophone     | Alexis  | 1960-11-29    | M     |      1 |
|        24 | Hochet      | Rick    | 1978-12-28    | M     |      1 |
|        25 | Liguili     | Guy     | 1996-03-18    | M     |      1 |
|        26 | Nouissement | Eva     | 1980-08-23    | F     |      1 |
|        27 | Qui         | Noah    | 1978-06-20    | M     |      2 |
|        28 | Bombeur     | Jean    | 1989-03-10    | M     |      2 |
|        29 | Indefil     | Bob     | 1990-11-09    | M     |      2 |
|        30 | Time        | Vincent | 1995-01-26    | M     |      2 |
+-----------+-------------+---------+---------------+-------+--------+
30 rows in set (0.001 sec)

BOOM 

#### Extra

How to Import Data Using Python

For importing data using Python, ensure you have the necessary libraries installed:

**Using pip:**

```sh
sudo pacman -S python-pip
```

1. **Install Required Libraries**:

   ```sh
   pip install pandas mysql-connector-python
   ```

**Using yay:**


1. **Install Required Libraries**:

    ```sh
    yay -S python-pandas python-mysql-connector
    ```

**Then Verify Installation**
After installing the packages, you can verify the installation by opening a Python shell and importing the libraries:

```sh
python
```

Then, within the Python shell, run:

```python
import pandas as pd
import mysql.connector
```
If there are no import errors, the installation was successful.

Create a Project Directory and Python Script
Create a Project Directory:

```sh
mkdir -p ~/SQL/Project
cd ~/SQL/Project
```

done :) 