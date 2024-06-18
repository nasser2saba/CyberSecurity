
# PYTHON FLASK DOCUMENTATION

Includes: 
- Step-by-step Guide
- Errors/Bugs & Fixes
- Explanation 
- Finished project?


## So...

To create a contact form in Python using Flask that meets the specified requirements (sanitization, validation, sending feedback), follow these steps:

### Step-by-Step Guide

#### 1. Setup Flask Application

Create a new directory for your project and initialize a Flask application. Make sure Flask is installed (you can install it using `sudo pacman -S python-flask` (I'm on Arch, use whatever) if not already installed).

Create a file named `app.py`:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flashing messages

# Sample countries list (you can expand this list as needed)
countries = ['Country A', 'Country B', 'Country C']

# Sample subjects list
subjects = ['Repair', 'Order', 'Others']

# Simple form data storage (in a real application, you would use a database)
form_data = {}

# Function to sanitize input to neutralize harmful encoding
def sanitize_input(input_str):
    # Replace any <script> tag with an empty string
    return re.sub(r'<script.*?>.*?</script>', '', input_str, flags=re.IGNORECASE)

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email)

# Route for displaying and handling the contact form
@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        country = request.form['country']
        message = request.form['message']
        gender = request.form['gender']
        selected_subjects = request.form.getlist('subject')

        # Sanitize inputs
        first_name = sanitize_input(first_name)
        last_name = sanitize_input(last_name)
        email = sanitize_input(email)
        country = sanitize_input(country)
        message = sanitize_input(message)

        # Validate inputs
        errors = []
        if not first_name:
            errors.append('First name is required.')
        if not last_name:
            errors.append('Last name is required.')
        if not email or not is_valid_email(email):
            errors.append('Valid email is required.')
        if not country:
            errors.append('Country is required.')
        if not message:
            errors.append('Message is required.')
        if not gender:
            errors.append('Gender is required.')
        if not selected_subjects:
            selected_subjects = ['Others']  # Default to "Others" if none selected

        if errors:
            for error in errors:
                flash(error, 'error')
            # Preserve valid responses in form_data for redisplaying
            form_data['first_name'] = first_name
            form_data['last_name'] = last_name
            form_data['email'] = email
            form_data['country'] = country
            form_data['message'] = message
            form_data['gender'] = gender
            form_data['selected_subjects'] = selected_subjects
            return redirect(url_for('contact_form'))
        else:
            # Store valid data for display in a "Thank you" page
            form_data['first_name'] = first_name
            form_data['last_name'] = last_name
            form_data['email'] = email
            form_data['country'] = country
            form_data['message'] = message
            form_data['gender'] = gender
            form_data['selected_subjects'] = selected_subjects
            return redirect(url_for('thank_you'))

    return render_template('contact_form.html', countries=countries, subjects=subjects)

# Route for displaying the "Thank you" page
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html', form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
```

#### 2. Create HTML Templates

Create two HTML templates in a subdirectory named `templates` in your project directory:

`templates/contact_form.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contact Form</title>
</head>
<body>
    <h2>Contact Form</h2>
    <form method="post">
        <div>
            <label for="first_name">First Name:</label>
            <input type="text" id="first_name" name="first_name" value="{{ form_data.get('first_name', '') }}" required>
        </div>
        <div>
            <label for="last_name">Last Name:</label>
            <input type="text" id="last_name" name="last_name" value="{{ form_data.get('last_name', '') }}" required>
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" value="{{ form_data.get('email', '') }}" required>
        </div>
        <div>
            <label for="country">Country:</label>
            <select id="country" name="country" required>
                <option value="" selected disabled>Select Country</option>
                {% for country in countries %}
                <option value="{{ country }}" {% if form_data.get('country') == country %}selected{% endif %}>{{ country }}</option>
                {% endfor %}
            </select>
        </div>
        <div>
            <label>Gender:</label><br>
            <input type="radio" id="male" name="gender" value="M" {% if form_data.get('gender') == 'M' %}checked{% endif %}>
            <label for="male">Male</label><br>
            <input type="radio" id="female" name="gender" value="F" {% if form_data.get('gender') == 'F' %}checked{% endif %}>
            <label for="female">Female</label><br>
        </div>
        <div>
            <label>Subjects:</label><br>
            {% for subject in subjects %}
            <input type="checkbox" id="{{ subject }}" name="subject" value="{{ subject }}" {% if subject in form_data.get('selected_subjects', []) %}checked{% endif %}>
            <label for="{{ subject }}">{{ subject }}</label><br>
            {% endfor %}
        </div>
        <div>
            <label for="message">Message:</label><br>
            <textarea id="message" name="message" rows="4" cols="50" required>{{ form_data.get('message', '') }}</textarea>
        </div>
        <div style="display:none">
            <label for="honeypot">Leave this field blank:</label>
            <input type="text" id="honeypot" name="honeypot">
        </div>
        <div>
            <button type="submit">Submit</button>
        </div>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
    <ul>
        {% for category, message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    {% endwith %}
</body>
</html>
```

`templates/thank_you.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Thank You</title>
</head>
<body>
    <h2>Thank you for contacting us.</h2>
    <p>Here is the summary of your information:</p>
    <ul>
        <li><strong>First Name:</strong> {{ form_data.get('first_name') }}</li>
        <li><strong>Last Name:</strong> {{ form_data.get('last_name') }}</li>
        <li><strong>Email:</strong> {{ form_data.get('email') }}</li>
        <li><strong>Country:</strong> {{ form_data.get('country') }}</li>
        <li><strong>Gender:</strong> {{ "Male" if form_data.get('gender') == 'M' else "Female" }}</li>
        <li><strong>Subjects:</strong> {% for subject in form_data.get('selected_subjects') %}{{ subject }} {% endfor %}</li>
        <li><strong>Message:</strong><br>{{ form_data.get('message') }}</li>
    </ul>
</body>
</html>
```

#### 3. Running the Application

Ensure you have Flask installed (`pip install Flask`), and then run your Flask application:

```sh
python app.py
```

Visit `http://127.0.0.1:5000/` in your web browser to access the contact form. Fill out the form, submit it, and you should see a "Thank you" page displaying the submitted information if validation passes.

### Explanation

- **Flask Routes**: Handles both GET and POST requests for displaying the form and processing form submissions.
- **HTML Templates**: `contact_form.html` renders the form and handles displaying validation errors. `thank_you.html` displays a summary of the submitted form data.
- **Sanitization**: The `sanitize_input` function uses regex to neutralize harmful encoding, specifically targeting `<script>` tags.
- **Validation**: Checks for mandatory fields and validates email format using regular expressions.
- **Flash Messages**: Used for displaying error messages next to their respective form fields.

This setup fulfills the requirements for a Flask-based contact form that performs server-side sanitization, validation, and provides feedback to the user. Adjustments can be made to expand


### Errors/Bugs & Fixes

Script wasn't able to access the templates, realised it was trying to access "template" folder while i had it saved as "Templates", welp

Then encountered issues tryina push the changes to github but it worked out just pulled origin main and push it again. 

Now tryna figure out why it still can't acces the freaking templates, bruh



ChatGPT troubleshoot: 

In your Flask application (app.py), verify that the render_template function is correctly referencing contact_form.html. Here's an example:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('contact_form.html')

if __name__ == '__main__':
    app.run(debug=True)
```