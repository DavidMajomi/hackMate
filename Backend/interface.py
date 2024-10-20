import pandas as pd
import sqlite3 as sql
from os import path
from sqlalchemy import create_engine
import datetime


ROOT = path.dirname(path.relpath(__file__))


def create_post(author, content):
    date_created = datetime.datetime.now()
    
    con = sql.connect(path.join(ROOT, "database.db"))
    cur = con.cursor()
    
    cur.execute("insert into posts (author, content, postdate) values(?, ?, ?)", (author, content, date_created))
    
    con.commit()
    con.close()
    
    
def delete_post():
    pass
    
    
    
def get_posts():
    con = sql.connect(path.join(ROOT, "database.db"))
    cur = con.cursor()
    
    cur.execute("SELECT * from posts")
    engine = create_engine("sqlite:///" + "database.db", echo=False)
    
    posts = pd.read_sql("SELECT * from posts", engine, index_col="id")
    
    return posts.to_json()



def create_profile(user_name, display_name, bio):
    date_created = datetime.datetime.now()
    
    con = sql.connect(path.join(ROOT, "database.db"))
    cur = con.cursor()
    cur.execute("insert into users (username, displayname, bio, dateofcreation) values(?, ?, ?, ?)", (user_name, display_name, bio, date_created))
    
    con.commit()
    con.close()



def edit_profile(user_name, display_name, bio):
    con = sql.connect(path.join(ROOT, "database.db"))
    cur = con.cursor()
    cur.execute(f"UPDATE users SET displayname = '{display_name}', bio = '{bio}' WHERE username = '{user_name}';")
    
    con.commit()
    con.close()


def get_profile_details(username):
    pass


def get_users_followers(username):
    pass


def get_users_following(username):
    pass


def get_users_posts(username):
    pass



