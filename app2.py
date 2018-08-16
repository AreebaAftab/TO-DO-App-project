# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 23:22:25 2018

@author: Areeba aftab
"""

from flask import Flask,\
render_template, url_for, \
redirect, request, session, redirect, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'axiom'

app.config['MONGO_URI'] = "mongodb://areeba:areeba11@ds119692.mlab.com:19692/axiom"

mongo = PyMongo(app)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=['GET','POST'])
def add():
    check=False
    if request.method == 'POST':
        dataInsert = mongo.db.tasks
        dataInsert.insert({'id': request.form['user'], 'title': request.form['pass'], 'description': request.form['description'], 'status': request.form['status']})
        check=True
    return render_template("add.html", ok=check)

@app.route("/delete", methods=['GET'])
def delete():
    check=False
    if request.method == 'GET':
        datadelete = mongo.db.tasks
        datadelete.delete({'id': request.form['user']})
        check=True
    return render_template("delete.html", ok=check)

@app.route("/API")
def api():
    dbAllData=mongo.db.tasks.find()
    alltasks=[]
    for tasks in dbAllData:
        alltasks.append({'description':tasks['description'],'task': tasks['title']})

    return jsonify({"task": alltasks})


if __name__=="__main__":
    app.run(debug=True)
