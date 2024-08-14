# app.py
from flask import Flask, request, redirect, url_for
from flask_cors import CORS
from routes.testRoute import test_route  # Import the blueprint
import interface
import secrets
import json
import os

app = Flask(__name__)
# app.register_blueprint(test_route)  # Register the blueprint

CORS(app)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_bytes(16) 


@app.route("/", methods = ['GET'])
@app.route("/home", methods = ['GET'])
def home():
    return "<h1> This is a demo home page </h1>"


@app.route("/sign_up", methods = ['GET', 'POST'])
def sign_up():
        
    if request.method == "GET":
        return "<h1> This is a test sign up route </h1>"

    
    if request.method == "POST":
        
        user_name = request.form.get('username')
        display_name = request.form.get('displayname')
        bio = request.form.get('bio')
        
        interface.create_profile(user_name, display_name, bio)
        
        return redirect(url_for('home'))
        

@app.route("/get_posts", methods = ['GET'])
def get_posts():
    return json.loads(interface.get_posts())



@app.route("/profile", methods = ['GET', 'POST'])
def profile():
    return "<h1> This a demo profile page </h1>"


@app.route("/edit_profile", methods = ['GET', 'POST'])
def edit_profile():
            
    if request.method == "GET":
        return "<h1> This is a test edit profile route </h1>"

    
    if request.method == "POST":
        
        user_name = request.form.get('username')
        display_name = request.form.get('displayname')
        bio = request.form.get('bio')
        
        interface.edit_profile(user_name, display_name, bio)
        
        return redirect(url_for('home'))


@app.route("/add_new_post", methods = ['GET', 'POST'])
def add_new_post():
    
    if request.method == "GET":
        return "<h1> Demo route to add new post </h1>"

    
    if request.method == "POST":
        
        author = request.form.get('author')
        content = request.form.get('content')
        
        interface.create_post(author, content)
        
        return redirect(url_for('home'))
        



if __name__ == '__main__':
    # app.run(debug = True)
    app.run(host='0.0.0.0', port=5000, debug = True)

