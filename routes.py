from flask import Flask
from flask import render_template , redirect,url_for,flash,get_flashed_messages
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

if (__name__ =="__main__"):
    app.run(debug=True)