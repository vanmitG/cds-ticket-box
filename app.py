# This is app.py, this is the main file called.
from src import app
from flask import render_template, redirect, url_for


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/admin')
def admin():
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)

# TODO disable this when running production because it does not let browser cache static content.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
