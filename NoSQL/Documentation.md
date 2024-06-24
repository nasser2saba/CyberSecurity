
# Installing and deploying MongoDB on Arch Linux

This is step-by-step documentation about everything that I've done to deploy the MongoDB.
If there were any errors during the process they'll be added with how I solved them.

If the command `mongo`does not work, use `mongosh`

## Setting up MONGO 

### Step 1: Install MongoDB

1. **Update the package database:**
    ```sh
    sudo pacman -Syu
    ```

2. **Install MongoDB:**
    MongoDB is available in the Arch User Repository (AUR). You can use an AUR helper like `yay` or `paru`. If you don't have `yay` installed, you can install it as follows:
    ```sh
    sudo pacman -S --needed git base-devel
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si
    ```

3. **Install MongoDB using `yay`:**
    ```sh
    yay -S mongodb-bin
    ```

### Step 2: Configure MongoDB

1. **Create the data directory:**

**This is done outside the /yay directory!!**

    ```sh
    sudo mkdir -p /var/lib/mongo
    sudo chown -R mongodb:mongodb /var/lib/mongo
    ```

2. **Create the log directory:**

    ```sh
    sudo mkdir -p /var/log/mongodb
    sudo chown -R mongodb:mongodb /var/log/mongodb
    ```

3. **Edit the MongoDB configuration file (`/etc/mongodb.conf`):**
    Ensure the following settings are in place:
    ```yaml
    storage:
      dbPath: /var/lib/mongo
    systemLog:
      destination: file
      path: /var/log/mongodb/mongod.log
    net:
      bindIp: 127.0.0.1
      port: 27017
    security:
      authorization: enabled
    ```

### Step 3: Start MongoDB

1. **Enable and start the MongoDB service:**
    ```sh
    sudo systemctl enable mongodb
    sudo systemctl start mongodb
    ```

2. **Check the status of the MongoDB service:**
    ```sh
    sudo systemctl status mongodb
    ```

### Step 4: Secure MongoDB

1. **Access the MongoDB shell:**
    ```sh
    mongo
    ```


I got an error here saying "mongo: command does not exist" 
Went down a whole rabbit hole tryna fix this. First it was files in one directory and not in the other, then it was a certain file that made mongo work in the shell that was missing, then it was that that package does not exist.
Currently updating all my packages and retrying to see if that package really does not exist and chatgpt is just messing around. 

Yep it really does not exist

Okay, half an hour later I believe it works .

I used https://www.mongodb.com/try/download/shell to download the shell instead of doing it through my terminal.
Chatgpt was tryna make me do some weird stuf changing the directory and blabla just to run mongosh. I ended up just navigating to the file in my terminal and starting mongosh through there. 
So basically if i run "mongo" in my terminal it won't work.
I'll have to either navigate to mongosh or type the entire path.


2. **Create an administrative user:**
    In the Mongo shell, switch to the admin database and create a user:
    ```js
    use admin
    db.createUser({
      user: "admin",
      pwd: "password",
      roles: [{ role: "userAdminAnyDatabase", db: "admin" }]
    })
    ```

3. **Restart MongoDB to apply the security changes:**
    ```sh
    sudo systemctl restart mongodb
    ```

### Step 5: Connect to MongoDB

1. **Using Mongo Shell:**
    ```sh
    mongo -u admin -p password --authenticationDatabase admin
    ```

Since this ain't working for me I'll be using alternatives


2. **Using MongoDB Compass:**
    - Download and install MongoDB Compass from the [official website](https://www.mongodb.com/try/download/compass).
    - Open Compass and enter the connection string (e.g., `mongodb://admin:password@localhost:27017`).

3. **Using Application Code:**
    - In your application, use a MongoDB driver (e.g., for Node.js, Python, Java, etc.) to connect to MongoDB. Here's an example in Node.js:
    ```javascript
    const { MongoClient } = require('mongodb');

    const uri = "mongodb://admin:password@localhost:27017";
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    async function run() {
        try {
            await client.connect();
            console.log("Connected to MongoDB");
        } finally {
            await client.close();
        }
    }
    run().catch(console.dir);
    ```


**FIGURED OUT ERROR**

Alright so, the issue was that whenever I tried to un mongo I'd use the mongo command in my terminal but I'd get met with an error that that command does not exist, turns out the correct command was **`mongosh`**


### Step 6: Monitor and Maintain MongoDB

1. **Monitor MongoDB:**
    - Use tools like MongoDB Compass, `mongostat`, and `mongotop` to monitor your MongoDB instance.

2. **Backup and Restore:**
    - Use `mongodump` to backup data:
    ```sh
    mongodump --out /path/to/backup
    ```

    - Use `mongorestore` to restore data:
    ```sh
    mongorestore /path/to/backup
    ```

3. **Regular Maintenance:**
    - Regularly update MongoDB to the latest version.
    - Monitor logs located at `/var/log/mongodb/mongod.log`.




## Using Mongo 
Now, I'll give 2 different Database examples, that are deployed on mongo. 


- Example 1: Deploying the SQL project on mongo 
- Example 2: E-commerce application 


## SQL student Database 

To deploy your MySQL database on MongoDB, you'll need to follow these general steps:

1. **Install MongoDB**: Ensure MongoDB is installed on your system.
2. **Export MySQL Data**: Export your MySQL data to a format that MongoDB can understand, such as JSON or CSV.
3. **Transform Data**: Transform the exported data to match MongoDB's document structure, if necessary.
4. **Import Data into MongoDB**: Use MongoDB tools to import the transformed data.
5. **Verify Data**: Ensure the data has been correctly imported and verify its integrity.

### Step-by-Step Guide

#### Step 1: Install MongoDB

If you don't have MongoDB installed, you can use a package manager like `yay` or `pacman` to install it on Arch Linux:

```sh
sudo pacman -S mongodb
```

#### Step 2: Export MySQL Data

Export your MySQL data to a JSON file. You can use a tool like `mysqldump` combined with `jq` or `python` to export and transform the data.

Here's an example using Python to export MySQL data to JSON:

1. **Install MySQL Connector for Python**:

    ```sh
    pip install mysql-connector-python
    ```

2. **Create a Python Script to Export Data**:

    ```python
    import mysql.connector
    import json

    # MySQL connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="becode"
    )

    cursor = conn.cursor(dictionary=True)

    # Query to select all data from students table
    cursor.execute("SELECT * FROM students")

    # Fetch all rows
    rows = cursor.fetchall()

    # Convert to JSON
    with open('students.json', 'w') as file:
        json.dump(rows, file, indent=4)

    cursor.close()
    conn.close()
    ```

    Replace `your_password` with your actual MySQL password. Save this script as `export_to_json.py` and run it:

    ```sh
    python export_to_json.py
    ```

    This will create a `students.json` file with your data.

#### Step 3: Transform Data (If Necessary)

If the exported JSON data needs to be transformed to match MongoDB's document structure, you can use a script to modify it. However, for basic structures, this step might not be necessary.

#### Step 4: Import Data into MongoDB

Use the `mongoimport` tool to import the JSON data into MongoDB.

1. **Start MongoDB**:

    ```sh
    sudo systemctl start mongodb
    ```

2. **Import the JSON File**:

    ```sh
    mongoimport --db becode --collection students --file students.json --jsonArray
    ```

#### Step 5: Verify Data

1. **Log in to MongoDB**:

    ```sh
    mongo
    ```

2. **Switch to the `becode` Database**:

    ```js
    use becode
    ```

3. **Verify the Data**:

    ```js
    db.students.find().pretty()
    ```

### Detailed Steps

Let's break down the steps in detail, assuming you have already created the JSON file `students.json`.

#### 1. Install MongoDB

Ensure MongoDB is installed on your system. If not, install it using:

```sh
sudo pacman -S mongodb
```

#### 2. Export MySQL Data to JSON

We used a Python script to export data. Ensure you have the `mysql-connector-python` package installed:

```sh
pip install mysql-connector-python
```

Create and run the Python script `export_to_json.py`:

```python
import mysql.connector
import json

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="becode"
)

cursor = conn.cursor(dictionary=True)

# Query to select all data from students table
cursor.execute("SELECT * FROM students")

# Fetch all rows
rows = cursor.fetchall()

# Convert to JSON
with open('students.json', 'w') as file:
    json.dump(rows, file, indent=4)

cursor.close()
conn.close()
```

Run the script:

```sh
python export_to_json.py
```

#### 3. Import Data into MongoDB

1. **Start MongoDB**:

    ```sh
    sudo systemctl start mongodb
    ```

2. **Import the JSON File**:

    ```sh
    mongoimport --db becode --collection students --file students.json --jsonArray
    ```

#### 4. Verify Data

1. **Log in to MongoDB**:

    ```sh
    mongo
    ```

2. **Switch to the `becode` Database**:

    ```js
    use becode
    ```

3. **Verify the Data**:

    ```js
    db.students.find().pretty()
    ```

This process will migrate the MySQL data to MongoDB. If you need to transform the data further to fit MongoDB's document model, you can do so using Python or another scripting language before importing.

### Ecommerce store

A MongoDB database for a simple e-commerce application. 
The database will include collections for users, products, and orders.

### Step-by-Step Guide to Create an E-commerce Database in MongoDB

#### Step 1: Access the MongoDB Shell
```sh
mongo -u admin -p password --authenticationDatabase admin
```

#### Step 2: Create and Switch to the Database
```js
use ecommerce
```

#### Step 3: Create Collections and Insert Documents

1. **Create the `users` collection:**
   ```js
   db.users.insertMany([
       {
           username: "johndoe",
           email: "john@example.com",
           password: "securepassword",
           address: {
               street: "123 Elm St",
               city: "Somewhere",
               state: "CA",
               zip: "90210"
           },
           created_at: new Date()
       },
       {
           username: "janedoe",
           email: "jane@example.com",
           password: "anotherpassword",
           address: {
               street: "456 Oak St",
               city: "Anywhere",
               state: "NY",
               zip: "10001"
           },
           created_at: new Date()
       }
   ]);
   ```

2. **Create the `products` collection:**
   ```js
   db.products.insertMany([
       {
           name: "Laptop",
           description: "A high performance laptop",
           price: 1200,
           category: "electronics",
           stock: 50,
           created_at: new Date()
       },
       {
           name: "Smartphone",
           description: "A latest model smartphone",
           price: 800,
           category: "electronics",
           stock: 100,
           created_at: new Date()
       },
       {
           name: "Coffee Maker",
           description: "A top-of-the-line coffee maker",
           price: 150,
           category: "home appliances",
           stock: 20,
           created_at: new Date()
       }
   ]);
   ```

3. **Create the `orders` collection:**
   ```js
   db.orders.insertMany([
       {
           user_id: ObjectId("60d9f9f5fc13ae1a92000001"),  // Replace with actual user ID
           products: [
               { product_id: ObjectId("60d9f9f5fc13ae1a92000002"), quantity: 1 },  // Replace with actual product ID
               { product_id: ObjectId("60d9f9f5fc13ae1a92000003"), quantity: 2 }   // Replace with actual product ID
           ],
           total: 1700,
           status: "shipped",
           created_at: new Date()
       },
       {
           user_id: ObjectId("60d9f9f5fc13ae1a92000002"),  // Replace with actual user ID
           products: [
               { product_id: ObjectId("60d9f9f5fc13ae1a92000001"), quantity: 1 }  // Replace with actual product ID
           ],
           total: 1200,
           status: "processing",
           created_at: new Date()
       }
   ]);
   ```

#### Step 4: Query the Database

1. **Find all users:**
   ```js
   db.users.find().pretty()
   ```

2. **Find all products in the "electronics" category:**
   ```js
   db.products.find({ category: "electronics" }).pretty()
   ```

3. **Find all orders for a specific user:**
   ```js
   db.orders.find({ user_id: ObjectId("60d9f9f5fc13ae1a92000001") }).pretty()  // Replace with actual user ID
   ```

#### Step 5: Update and Delete Documents

1. **Update a user's email:**
   ```js
   db.users.updateOne(
       { username: "johndoe" },
       { $set: { email: "newjohn@example.com" } }
   );
   ```

2. **Delete a product:**
   ```js
   db.products.deleteOne({ name: "Coffee Maker" });
   ```

3. **Update the status of an order:**
   ```js
   db.orders.updateOne(
       { _id: ObjectId("60d9f9f5fc13ae1a92000004") },  // Replace with actual order ID
       { $set: { status: "delivered" } }
   );
   ```

### Step 6: Ensure Data Integrity

1. **Create indexes for faster queries:**
   ```js
   db.users.createIndex({ email: 1 }, { unique: true });
   db.products.createIndex({ name: 1 }, { unique: true });
   db.orders.createIndex({ user_id: 1 });
   ```

2. **Validate data with schema validation (optional):**
   ```js
   db.createCollection("users", {
       validator: {
           $jsonSchema: {
               bsonType: "object",
               required: ["username", "email", "password", "created_at"],
               properties: {
                   username: { bsonType: "string" },
                   email: { bsonType: "string" },
                   password: { bsonType: "string" },
                   created_at: { bsonType: "date" }
               }
           }
       }
   });
   ```





Anddd we're doneeee.