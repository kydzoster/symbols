import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import re
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'symbols'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@my1stcluster-phyn3.mongodb.net/symbols?retryWrites=true&w=majority'
MONGODB_NAME = os.environ.get('MONGODB_NAME')

mongo = PyMongo(app)


# Index.html (Homepage)
@app.route('/')
@app.route('/show_words')
def show_words():
    return render_template("index.html", words=mongo.db.words.find())


# Browse Words Page
@app.route('/get_words')
def get_words():
    return render_template(
        "words.html", words=mongo.db.words.find().sort("word_name"))


# New Word Page
@app.route('/add_word')
def add_word():
    return render_template(
        'addword.html', categories=mongo.db.categories.find())


# Function to inject word in to database
@app.route('/insert_word', methods=['POST'])
def insert_word():
    words = mongo.db.words
    new_word = request.form.get("word_name")
    # If stmnt to prevent duplicate words
    if words.count_documents({'word_name': new_word}, limit=1) == 0:
        words.insert_one(request.form.to_dict())
    else:
        flash("This item already exists in the database!")
    return redirect(url_for('get_words'))


# Edit Word Page
@app.route('/edit_word/<word_id>')
def edit_word(word_id):
    the_word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    all_categories = mongo.db.categories.find()
    return render_template(
        'editword.html', word=the_word, categories=all_categories)


# Function to update word_name; category_name; word_definition in database
@app.route('/update_word/<word_id>', methods=["POST"])
def update_word(word_id):
    words = mongo.db.words
    words.update({'_id': ObjectId(word_id)}, {
        'category_name': request.form.get('category_name'),
        'word_name': request.form.get('word_name'),
        'word_definition': request.form.get('word_definition')

    })
    return redirect(url_for('get_words'))


# Function to delete words from database
@app.route('/delete_word/<word_id>')
def delete_word(word_id):
    mongo.db.words.remove({'_id': ObjectId(word_id)})
    return redirect(url_for('get_words'))


# Manage Categories Page
@app.route('/get_categories')
def get_categories():
    return render_template(
        'categories.html', categories=mongo.db.categories.find().sort(
            "category_name"))
    # .sort added to display categories in alphabetical order


# Edit Categories Page
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template(
        'editcategory.html', category=mongo.db.categories.find_one(
            {'_id': ObjectId(category_id)}))


# Function to update category in database
@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


# Function to inject category in database
@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = mongo.db.categories
    new_category = request.form.get("category_name")
    # If stmnt to prevent duplicate categories
    if (category_doc.count_documents(
            {'category_name': new_category}, limit=1) == 0):
            category_doc.insert_one(request.form.to_dict())
    else:
        flash("This item already exists in the database!")
    return redirect(url_for('get_categories'))


# Add Category Page
@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


# Function to delete category frm database
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


# GET METHOD for Search Bar
@app.route('/get_search')
def get_search():
    """
    Route to accept a GET request to perform
    a search
    """
    query = request.args.get('q')  # Grab the arugments via GET request
    print(query)

    results = mongo.db.words.find(
        {"word_name": {"$regex": query, "$options": 'i'}})
    return render_template(
        'search.html',  query=results)  # Pass the results to the view


# Function for Individual Letter search
@app.route('/get_letters/<letter>')
def get_letters(letter):
    print(letter)

    results = mongo.db.words.find(
        {"word_name": {"$regex": letter, "$options": 'i'}})

    return render_template('searchletter.html', letter=results)
    print(word_name)
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
