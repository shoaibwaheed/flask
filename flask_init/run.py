# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:03:49 2018

@author: swaheed
"""
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    #host=os.setenv('IP' ,'0.0.0.0')
    #port=int(os.setenv('PORT',5000))
    #app.run(host,port=port)
    app.run()
               