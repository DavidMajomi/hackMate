# app.py
from flask import Flask, session,request, redirect, url_for
from routes.testRoute import test_route  # Import the blueprint
import interface
import secrets
import json


app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_bytes(16) 

@app.route('/profile')
def profile():
    user_info = session.get('profile')
    return f'Hello, {user_info["name"]}!'



@app.route('/api/register', ['POST'])
def register():
    user_name = request.form.get('username')
    display_name = request.form.get('displayname')
    bio = request.form.get('bio')
    password = request.form.get('password')
    
    success = interface.create_profile(user_name, display_name, bio, password)
    
    if success == True:
        return {"message": "Succcessful Registration","userId": "string"}
    else:
        return {"message": "Failed Registration","userId": "string"}
  


@app.route('api/login', ['POST'])
def login():
    user_name = request.form.get('username')
    password = request.form.get('password')
    
    success = interface.login(user_name, password)
    
    if success == True:
        return {"message": "Succcessful Login","userId": "string"}
    else:
        return {"message": "Failed Registration","userId": "string"}
    
    
    
@app.route('/logout')
def logout():
    
   session.pop('username', None)
   return redirect(url_for('login'))


@app.route("/get_posts", methods = ['GET'])
def get_posts():
    return json.loads(interface.get_posts())



@app.route("/get_profile_details", methods = ['GET'])
def profile_details():
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

