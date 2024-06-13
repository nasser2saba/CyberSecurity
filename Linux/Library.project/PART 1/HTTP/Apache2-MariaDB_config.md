
# CONFIGURING HTTP (Apache) Mariadb

for this part, there were multiple ways to use configure it, through Apache and Nginx
I worked with Apache but added some commands for Nginx if i'm not mistaken. 
Incase I'm mistaken here's a smiley :)


! CHECK SUPPORT FILE !
I had an error who was i managed to fix, could be that by following the same steps you'll end up with the same error so check the support file bro.


#

Install Apache or Nginx and MariaDB:
$ sudo apt update
$sudo apt install apache2 php mariadb-server php-mysql

Enable necessary Apache modules:
$sudo a2enmod rewrite
$sudo systemctl restart apache2

Secure MariaDB Installation:
Run the MySQL/MariaDB secure installation script
$sudo mysql_secure_installation
Follow the prompts to secure your MariaDB installation
-enter current passw
-set root passw
-remove anonymous users -y
-disallow root login remotely -y 
-remoce test database and acces to it -y
-reload privilege tables to apply changes -y
all the yes choices are recommended for security reasons :)



Create a Database and User:

Log into the MariaDB shell
$ sudo mysql -u root -p

Create a new database and user:

CREATE DATABASE mydatabase;
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'localhost';
FLUSH PRIVILEGES;

Replace 'mydatabase', 'myuser', and 'password' with your preferred values.



for examle)

CREATE DATABASE librarydb;
CREATE USER 'libraryuser'@'localhost' IDENTIFIED BY 'Librarian123!';
GRANT ALL PRIVILEGES ON librarydb.* TO 'libraryuser'@'localhost';
FLUSH PRIVILEGES;

to exit mariadb, type: exit;


Configure Apache to Serve PHP Files:

Edit Apache configuration file
$sudo nano /etc/apache2/sites-available/000-default.conf

Add the following lines inside the <VirtualHost> block:

<Directory /var/www/html>
    Options Indexes FollowSymLinks
    AllowOverride All
    Require all granted
</Directory>

Create a PHP Script to Access MariaDB:

Create a PHP script in /var/www/html directory, for example index.php

<?php
$servername = "localhost";
$username = "myuser";
$password = "password";
$dbname = "mydatabase";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
$conn->close();
?>


for example)

<?php
// Database credentials
$servername = "localhost";
$username = "libraryuser";
$password = "Librarian123!";
$dbname = "librarydb";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Connected successfully";

// Close connection
$conn->close();
?>


Restart Apache:

$ sudo systemctl restart apache2




to test if it's working: 

$ sudo systemctl status apache2

Open a web browser on a device connected to the same network as your server.

Enter the IP address or domain name of your server in the address bar. For example:

http://your_server_ip/index.php