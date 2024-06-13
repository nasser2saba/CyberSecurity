

# Regex - Exercises


## 1. Create a regex that finds integers without size limit.


_**s = "sssgdds8sfsfs"**_


solve: 

Use the re module in Python. An integer can be represented by the regex pattern \d+, which matches one or more digits.



```python
import re

s = "sssgdds8sfsfs"
pattern = r'\d+'

matches = re.findall(pattern, s)
print(matches)

```

This code will find all sequences of digits in the string s and print them as a list.


     
## 2. Create a regex that finds negative integers without size limit.


_**s = "sssgdds-8sfsfs"**_ 



solve: 
-> use a pattern that looks for an optional minus sign followed by one or more digits.



```python 
import re

s = "sssgdds-8sfsfs"
pattern = r'-\d+'  # This pattern matches a minus sign followed by one or more digits

matches = re.findall(pattern, s)  # Finds all matches of the pattern in the string
print(matches)  # Output the list of matches

```

This pattern r'-\d+' works as follows:

- '-' matches the minus sign.
- \d+ matches one or more digits.

     
## 3. Create a regex that finds (positive or negative) integers without size limit.


_**s = "sssgdds-8s8fsfs"**_


solution: 

-> use a pattern that looks for an optional minus sign followed by one or more digits. The minus sign should be optional to also match positive integers.


```python
import re

s = "sssgdds-8s8fsfs"
pattern = r'-?\d+'  # This pattern matches an optional minus sign followed by one or more digits

matches = re.findall(pattern, s)  # Finds all matches of the pattern in the string
print(matches)  # Output the list of matches

```

This pattern r'-?\d+' works as follows:

- -?  matches zero or one minus sign.
- \d+ matches one or more digits.

     
## 4. Capture all the numbers of the following sentence :


_**text = "21 scouts and 3 tanks fought against 4,003 protestors, so the manager was not 100.00% happy."**_ 


solution: 

-> use a regular expression that matches both integer and floating-point numbers.


```python
import re

text = "21 scouts and 3 tanks fought against 4,003 protestors, so the manager was not 100.00% happy."
pattern = r'\d[\d,]*\.?\d*'

matches = re.findall(pattern, text)
print(matches)

```

so: 
- \d matches any digit.
- [\d,]* matches zero or more digits or commas (to capture numbers like 4,003).
- \.? matches zero or one decimal point.
- \d* matches zero or more digits (to capture the fractional part of numbers).

the solution: 
- Import the re module.
- Define the text string.
- Define the regex pattern to match numbers.
- Use re.findall() to find all matches of the pattern in the text.
- Print the matches.
     
## 5. Find all words that end with 'ly'.


_**text = "He had prudently disguised himself but was quickly captured by the police."**_


solution: 
->  use a regular expression that looks for word boundaries followed by any characters ending with 'ly'.


```python
import re

text = "He had prudently disguised himself but was quickly captured by the police."
pattern = r'\b\w+ly\b'

matches = re.findall(pattern, text)
print(matches)
```

When you run this code, it will find and print all the words in the given sentence that end with 'ly'.

Explanation of the pattern r'\b\w+ly\b':

- \b matches a word boundary.
- \w+ matches one or more word characters (letters, digits, or underscores).
- ly matches the exact characters 'ly'.
- \b matches another word boundary to ensure 'ly' is at the end of a word.
- This pattern ensures that only whole words ending with 'ly' are matched.

Let's break down the solution step by step:

- Import the re module.
- Define the text string.
- Define the regex pattern to match words ending with 'ly'.
- Use re.findall() to find all matches of the pattern in the text.
- Print the matches.

     
## 6. License plate number

_A license plate consists of 2 capital letters, a dash ('-'), 3 digits, a dash ('-') and finally 2 capital letters. Write a script to check that an input string is a license plate.
If it's correct, print "good". If it's not correct, print "Not good"._


_plate = input("Enter your license plate number: ")_

solution: 



```python
import re

plate = input("Enter your license plate number: ")
pattern = r'^[A-Z]{2}-\d{3}-[A-Z]{2}$'

if re.match(pattern, plate):
    print("good")
else:
    print("Not good")
```

Explanation of the pattern `r'^[A-Z]{2}-\d{3}-[A-Z]{2}$'`:
- `^` asserts the start of the string.
- `[A-Z]{2}` matches exactly two capital letters.
- `-` matches the dash character.
- `\d{3}` matches exactly three digits.
- `-` matches another dash character.
- `[A-Z]{2}` matches exactly two capital letters.
- `$` asserts the end of the string.

This pattern ensures that the input string conforms exactly to the required license plate format.


When you run this script, it will prompt you to enter a license plate number and will print "good" if the input matches the required format, or "Not good" if it does not.
     
## 7 . Address IPV4
_An IPv4 address is composed of 4 numbers between 0 and 255 separated by '.'
Write a script to verify that a string entered is that of an IPv4 address._


_ip = input("Enter your IP address :" )_


solution:

To verify that a string entered is a valid IPv4 address, you can use a regular expression that checks if each of the four numbers in the address is between 0 and 255. Here's a Python script to achieve this:

```python
import re

ip = input("Enter your IP address: ")

# Pattern to match a valid IPv4 address
pattern = r'^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$'

if re.match(pattern, ip):
    print("Valid IPv4 address")
else:
    print("Invalid IPv4 address")
```

Explanation of the pattern `r'^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$'`:
- `^` asserts the start of the string.
- `((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}` matches the first three octets:
  - `25[0-5]` matches numbers from 250 to 255.
  - `2[0-4]\d` matches numbers from 200 to 249.
  - `1\d{2}` matches numbers from 100 to 199.
  - `[1-9]?\d` matches numbers from 0 to 99 (allowing optional leading zeroes).
  - `\.` matches the dot separator.
- `(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)` matches the fourth octet.
- `$` asserts the end of the string.


This script will prompt the user to enter an IP address and will print "Valid IPv4 address" if the input matches the IPv4 format, or "Invalid IPv4 address" if it does not.
     
## 8. Valid Mail
_An email is composed of alphanumeric characters followed by @ and a domain name.
Write a script that checks that the string entered by a user is indeed that of an email, otherwise ask him to re-enter it again (until he gets a valid email)._


solution: 

If the entered string is not a valid email address, it will prompt the user to re-enter it until a valid email is provided:

```python

import re

while True:
    mail = input("Enter your email: ")
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', mail):
        print("Valid email!")
        break
    else:
        print("Invalid email. Please enter a valid email address.")
```

This script uses the `re.match()` function to check if the entered string matches the pattern of a valid email address. If it does, it prints "Valid email!" and exits the loop. If not, it prints "Invalid email. Please enter a valid email address." and prompts the user to enter the email again.
mail = input("Enter your email :" )
     
## 9. Valid Password
_Write an additional script that verifies the password (obviously if the email is valid) where the only specificity of the password is that it has to contain at least 6 characters._


_password = input("Enter your password :" )_


solution: 


```python
while True:
    password = input("Enter your password: ")
    if len(password) >= 6:
        print("Valid password!")
        break
    else:
        print("Password must contain at least 6 characters. Please enter a valid password.")
```

This script prompts the user to enter a password and checks if the length of the password is at least 6 characters. If the password meets this requirement, it prints "Valid password!" and exits the loop. Otherwise, it prints "Password must contain at least 6 characters. Please enter a valid password." and prompts the user to enter the password again.
     
## 10. Valid Password bis
_The password must now contain at least 6 characters AND_

_at least one lowercase letter AND
at least one uppercase letter AND
at least one number AND
at least one special character (among $#@)._

_password = input("Enter your password :" )_

solution: 

To meet the new requirements for a valid password, you can utilize regular expressions to check for the presence of at least one lowercase letter, one uppercase letter, one number, and one special character among `$#@`.

```python
import re

while True:
    password = input("Enter your password: ")
    if len(password) >= 6 and re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]+$', password):
        print("Valid password!")
        break
    else:
        print("Password must contain at least 6 characters, one lowercase letter, one uppercase letter, one number, and one special character ($#@). Please enter a valid password.")
```

This script uses a regular expression pattern with positive lookahead assertions to ensure that the password contains at least one lowercase letter (`(?=.*[a-z])`), one uppercase letter (`(?=.*[A-Z])`), one number (`(?=.*\d)`), and one special character from the set `#$@` (`(?=.*[$#@])`). It also checks that the password has a length of at least 6 characters. If the password meets all these requirements, it prints "Valid password!" and exits the loop. Otherwise, it prints a message asking the user to enter a valid password.

      
## 11. Search by groups
_It is possible to search by groups, and it is very powerful!
?P<x>\w+ means the capture of a "group" named x, this group is composed of at least (+) one alphanumeric character (\w)._


_m = re.search(
    "Welcome to (?P\w+) ! You are (?P\d+) years old ?",
    "Welcome to Olivier ! You are 32 years old ?",
)
print(m.group("where"))
print(m.group("age"))_


solution: 

To correctly search by groups using named groups in a regex pattern, you need to ensure that the pattern is defined properly.the pattern is not correctly formatted. Here is the corrected version:

```python
import re

# Correct pattern with named groups 'where' and 'age'
pattern = r"Welcome to (?P<where>\w+) ! You are (?P<age>\d+) years old ?"

# Sample text
text = "Welcome to Olivier ! You are 32 years old ?"

# Perform the search
m = re.search(pattern, text)

# Check if the search was successful and print the captured groups
if m:
    print(m.group("where"))
    print(m.group("age"))
else:
    print("No match found.")
```

Explanation:
- `(?P<where>\w+)` captures one or more alphanumeric characters and names this group `where`.
- `(?P<age>\d+)` captures one or more digits and names this group `age`.

This code will capture "Olivier" as the `where` group and "32" as the `age` group from the provided text.


## Another Example
_m = re.search(
    "^(?P\w*)[.]?(?P\w*)@(?P\w+)[.](?P\w+$)",
    "audrey.boulevart@benextcomapgny.com",
)
if m is not None:
    print(m.group("who"))
    print(m.group("who2"))
    print(m.group("operator"))
    print(m.group("zone"))_
     
_Load the file ./data/mail.txt and clean it with the regex. The goal is to retrieve the last name, first name, operator and zone, as in the previous example. Store each of those into their own separate list._


_list_mail = open("./data/mail.txt")_


solution: 
To achieve the task of extracting the last name, first name, operator, and zone from email addresses in a file, we need to use a regular expression with named groups:

1. Load the file.
2. Apply the regex to extract the required information.
3. Store each part (last name, first name, operator, and zone) into separate lists.

First, we'll correct the regex pattern and then write the full script to process the file `./data/mail.txt`.

**Corrected Regex Pattern**
```regex
^(?P<first_name>\w+)[.]?(?P<last_name>\w*)@(?P<operator>\w+)[.](?P<zone>\w+)$
```

**Full Script**
```python
import re

# Define the regex pattern with named groups
pattern = r"^(?P<first_name>\w+)[.]?(?P<last_name>\w*)@(?P<operator>\w+)[.](?P<zone>\w+)$"

# Initialize lists to store the extracted information
first_names = []
last_names = []
operators = []
zones = []

# Open and read the file
with open('./data/mail.txt', 'r') as file:
    lines = file.readlines()

# Process each line (email address) in the file
for line in lines:
    line = line.strip()  # Remove any leading/trailing whitespace
    m = re.search(pattern, line)
    if m:
        first_names.append(m.group("first_name"))
        last_names.append(m.group("last_name"))
        operators.append(m.group("operator"))
        zones.append(m.group("zone"))

# Print the results
print("First Names:", first_names)
print("Last Names:", last_names)
print("Operators:", operators)
print("Zones:", zones)
```

**Explanation**
1. **Regex Pattern**: The regex pattern captures the first name, last name, operator, and zone from an email address.
   - `(?P<first_name>\w+)`: Captures the first name.
   - `[.]?`: Optionally matches a dot.
   - `(?P<last_name>\w*)`: Captures the last name.
   - `@`: Matches the '@' character.
   - `(?P<operator>\w+)`: Captures the operator (e.g., email service provider).
   - `[.]`: Matches a dot.
   - `(?P<zone>\w+)`: Captures the zone (e.g., 'com', 'org').
2. **File Handling**: The script opens the file `./data/mail.txt`, reads each line, and applies the regex pattern to extract the required information.
3. **Storing Results**: The extracted information is stored in separate lists (`first_names`, `last_names`, `operators`, `zones`).

### Running the Script
Ensure the file `./data/mail.txt` is available and contains email addresses in each line. Then, run the script to extract and print the desired information.

     
## 12. Another way of doing things.


_mail = "audrey.boulevart@benextcomapgny.com"
splitMail = mail.replace(".", " ").split("@").copy()_

_firstName = []
name = []
ope = []
zone = []_

_firstName.append(splitMail[0].split()[0])
name.append(splitMail[0].split()[-1])
ope.append(splitMail[1].split()[0])
zone.append(splitMail[1].split()[-1])_

_firstName, name, ope, zone_
     
_Repeat the previous exercise with this new formula and compare the length of your lists with those of the previous exercise.
What do you notice ?_

Solution:

**New Approach**
The new approach involves manually splitting and processing the email string:
1. Replace dots with spaces.
2. Split the email at the "@" character.
3. Extract the first name, last name, operator, and zone manually.



**Script Using the New Approach**
```python
# Define lists to store the extracted information
first_names_manual = []
last_names_manual = []
operators_manual = []
zones_manual = []

# Open and read the file
with open('./data/mail.txt', 'r') as file:
    lines = file.readlines()

# Process each line (email address) in the file using the new approach
for line in lines:
    mail = line.strip()  # Remove any leading/trailing whitespace
    splitMail = mail.replace(".", " ").split("@").copy()
    
    first_names_manual.append(splitMail[0].split()[0])
    last_names_manual.append(splitMail[0].split()[-1])
    operators_manual.append(splitMail[1].split()[0])
    zones_manual.append(splitMail[1].split()[-1])

# Print the results
print("First Names (Manual):", first_names_manual)
print("Last Names (Manual):", last_names_manual)
print("Operators (Manual):", operators_manual)
print("Zones (Manual):", zones_manual)

# Compare with the previous approach
print("Length Comparison:")
print("First Names:", len(first_names_manual), "vs", len(first_names))
print("Last Names:", len(last_names_manual), "vs", len(last_names))
print("Operators:", len(operators_manual), "vs", len(operators))
print("Zones:", len(zones_manual), "vs", len(zones))
```

**Compare the Results**
1. **Run the New Approach**: The script processes the email addresses and stores the information in separate lists.
2. **Run the Previous Approach**: Ensure the previous regex-based script is executed to store the extracted information in the lists `first_names`, `last_names`, `operators`, and `zones`.
3. **Compare the Lengths**: Print the lengths of the lists from both approaches to compare them.

**Expected Outcome**
The lengths of the lists from both approaches should match if both methods correctly process all email addresses. If there's a discrepancy, it could indicate an issue with one of the methods.

**Complete Comparison Script**
Here's a combined script to execute both approaches and compare the results:

```python
import re

# Define regex pattern
pattern = r"^(?P<first_name>\w+)[.]?(?P<last_name>\w*)@(?P<operator>\w+)[.](?P<zone>\w+)$"

# Initialize lists for the regex approach
first_names = []
last_names = []
operators = []
zones = []

# Initialize lists for the manual approach
first_names_manual = []
last_names_manual = []
operators_manual = []
zones_manual = []

# Open and read the file
with open('./data/mail.txt', 'r') as file:
    lines = file.readlines()

# Process each line in the file using both approaches
for line in lines:
    line = line.strip()  # Remove any leading/trailing whitespace
    
    # Regex approach
    m = re.search(pattern, line)
    if m:
        first_names.append(m.group("first_name"))
        last_names.append(m.group("last_name"))
        operators.append(m.group("operator"))
        zones.append(m.group("zone"))
    
    # Manual approach
    splitMail = line.replace(".", " ").split("@").copy()
    first_names_manual.append(splitMail[0].split()[0])
    last_names_manual.append(splitMail[0].split()[-1])
    operators_manual.append(splitMail[1].split()[0])
    zones_manual.append(splitMail[1].split()[-1])

# Print the results from both approaches
print("First Names (Regex):", first_names)
print("Last Names (Regex):", last_names)
print("Operators (Regex):", operators)
print("Zones (Regex):", zones)

print("First Names (Manual):", first_names_manual)
print("Last Names (Manual):", last_names_manual)
print("Operators (Manual):", operators_manual)
print("Zones (Manual):", zones_manual)

# Compare the lengths
print("Length Comparison:")
print("First Names:", len(first_names_manual), "vs", len(first_names))
print("Last Names:", len(last_names_manual), "vs", len(last_names))
print("Operators:", len(operators_manual), "vs", len(operators))
print("Zones:", len(zones_manual), "vs", len(zones))
```

By running this script, you can directly compare the results of both approaches and verify their accuracy.