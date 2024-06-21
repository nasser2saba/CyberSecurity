

#!/bin/bash

    # Database credentials
    USER="root"
    PASSWORD=
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