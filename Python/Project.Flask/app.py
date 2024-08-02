from flask import Flask, render_template, request, redirect, url_for, flash, session
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flashing messages

# Sample countries list (you can expand this list as needed)
countries = ['Country A', 'Country B', 'Country C']

# Sample subjects list
subjects = ['Repair', 'Order', 'Others']

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
    form_data = {}  # Initialize form_data to an empty dictionary

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

        form_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'country': country,
            'message': message,
            'gender': gender,
            'selected_subjects': selected_subjects
        }

        if errors:
            for error in errors:
                flash(error, 'error')
            # Preserve valid responses in form_data for redisplaying
            return render_template('contact_form.html', countries=countries, subjects=subjects, form_data=form_data)
        else:
            # Store valid data for display in a "Thank you" page
            session['form_data'] = form_data
            return redirect(url_for('thank_you'))
       
    return render_template('contact_form.html', countries=countries, subjects=subjects, form_data=form_data)


# Route for displaying the "Thank you" page
@app.route('/thank-you')
def thank_you():
    form_data = session.get('form_data', {})
    return render_template('thank_you.html', form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
