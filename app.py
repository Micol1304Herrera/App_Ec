from flask import Flask
from flask import render_template

app = Flask(__name__)




@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html')