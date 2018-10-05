# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:03:49 2018

@author: swaheed
"""
import os
from flask import Flask,url_for,request

app = Flask(__name__)

@app.route("/")
def index():
    return url_for('show_user_profile', username='someone')

@app.route('/login',methods=['GET'])
def login():
    if request.values:
        return 'username is ' + request.values['username']
    else:
        return '<form method ="get" action =/login"> <input ="text" name = "username"/><p><button type="submit">Submit</button'


@app.route("/user/<username>")
def show_user_profile(username):
    #show the userprofile for that user
    return "User " + str(username) 

@app.route("/hello")
def hello_world():
    return 'hello world 2'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show a post gven an id, post id must be an integer
    return "Post " + str(post_id)


if __name__ == '__main__':
    #host=os.setenv('IP' ,'0.0.0.0')
    #port=int(os.setenv('PORT',5000))
    #app.run(host,port=port)
    app.debug = True
    #import pdb;pdb.set_trace()
    app.run(debug=True)
               