import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'symbols'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@my1stcluster-phyn3.mongodb.net/symbols?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_index')
def get_index():
    return render_template("index.html")


@app.route('/get_symbols')
def get_symbols():
    return render_template("symbols.html")


@app.route('/get_signup')
def get_signup():
    return render_template("signup.html")


@app.route('/get_login')
def get_login():
    return render_template("login.html")


@app.route('/get_contact')
def get_contact():
    return render_template("contact.html")


@app.route('/get_account')
def get_account():
    return render_template("account.html")


@app.route('/get_add')
def get_add():
    return render_template("add.html")


@app.route('/get_edit')
def get_edit():
    return render_template("edit.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
