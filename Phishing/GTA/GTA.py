from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='Templates', static_folder='static')

@app.route('/')
def log_in():
    return render_template('log_in.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you can save the username and password to a database, file, or session
        # For example, you can store it in a session:
        # session['username'] = username
        # session['password'] = password
        return redirect(url_for('troll'))  # Redirect to another page after login
    return redirect(url_for('log_in'))  # Redirect to login page if method is not POST

@app.route('/troll')
def troll():
    return render_template('troll.html')

if __name__ == '__main__':
    app.run(debug=True)
