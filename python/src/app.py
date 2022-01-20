# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~
    A microblog example application written as Flask tutorial with
    Flask and sqlite3.
    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import with_statement
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_xmlrpcre.xmlrpcre import XMLRPCHandler, Fault

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.secret_key = SECRET_KEY
app.debug = DEBUG


@app.route('/')
def show_entries():
    return {"statusCode": 200, "msg": "ok"}




api = XMLRPCHandler('api')
api.connect(app, '/api')
# flaskr = api.namespace('flaskr')

@api.register
def new_post(text):
    return {"statusCode": 200, "msg": text}

@api.register
def get_posts():
    return {"statusCode": 200, "msg": "ok"}

if __name__ == '__main__':
    app.run()
