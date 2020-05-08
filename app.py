import os
from flask import Flask, flash, render_template, redirect, request, url_for, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'project'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@my1stcluster-phyn3.mongodb.net/project?retryWrites=true&w=majority'
app.config['SECRET_KEY'] = '57ffea7681cec524fff700193e5cdc11'
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWYZ"

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", letters=ALPHABET)


@app.route('/symbols')
def symbols():
    return render_template("symbols.html", letters=ALPHABET, symbols=mongo.db.symbols.find())


@app.route('/add_symbol')
def add_symbol():
    return render_template('add_symbol.html', letters=ALPHABET,
    # This line will find all Countries in MongoDB
    categories=mongo.db.categories.find())

@app.route('/insert_symbol', methods=['GET', 'POST'])
def insert_symbol():
    word = request.form['category_name'].lower()
    symbol_name = request.form['symbol_name'].lower()
    symbol_description = request.form['symbol_description'].lower()
    symbols = mongo.db.symbols
    all_symbols = mongo.db.symbols.find()
    all_words = [entry['category_name'] for entry in all_symbols]
    

    if word[0].upper() not in ALPHABET:
        flash('A word must start with a letter!')
        return redirect(url_for('add_symbol'))
    
    symbols.insert_one({
            'category_name': word,
            'letter': word[0].upper(),
            'symbol_name': symbol_name,
            'symbol_description': symbol_description
        })
    flash(("Entry '{}' successfully added!").format(word))
    return redirect(url_for('symbols',word=word))


# This function will find properties for symbols by its id with the help of ObjectId
@app.route('/edit_symbol/<symbol_id>')
def edit_symbol(symbol_id):
    the_symbol = mongo.db.symbols.find_one({'_id': ObjectId(symbol_id)})
    return render_template('edit_symbol.html', symbol=the_symbol)


@app.route('/update_symbol/<symbol_id>', methods=["POST"])
def update_symbol(symbol_id):
    symbols = mongo.db.symbols
    symbols.update({'_id': ObjectId(symbol_id)},
    {
        'category_name':request.form.get('category_name'),
        'letter': request.form.get('letter'),
        'symbol_name':request.form.get('symbol_name'),
        'symbol_description': request.form.get('symbol_description')
    })
    return redirect(url_for('symbols'))


@app.route('/delete_symbol/<symbol_id>')
def delete_symbol(symbol_id):
    mongo.db.symbols.remove({'_id': ObjectId(symbol_id)})
    return redirect(url_for('symbols'))


@app.route('/categories')
def categories():
    return render_template('categories.html', letters=ALPHABET,
    categories=mongo.db.categories.find())


# This function will find properties for countries by its id with the help of ObjectId
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('edit_category.html',
    category=mongo.db.categories.find_one())


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update({'_id': ObjectId(category_id)},
    {'category_name': request.form.get('category_name')})
    return redirect(url_for('categories'))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('categories'))


@app.route('/register')  # For the register button
def open_register():
    return render_template('register.html', letters=ALPHABET, title='Register')


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})
        if existing_user is None:
            hash_password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({
                'username': request.form['username'],
                'password': hash_password
                })
            flash('Your account has been created successfuly! You can now Login!', 'success')
            return redirect(url_for('login'))
        else:
            flash('This email is already taken! Please try a different email!', 'danger')
        return render_template('register.html')


@app.route('/login')
def open_login():
    return render_template('login.html', letters=ALPHABET, title='Login')


@app.route('/login', methods=["POST", "GET"])
def login():
    users = mongo.db.users
    login_user = users.find_one({'username': request.form['username']})
    if login_user and bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            flash('You have been logged in!', 'success')
            return redirect(url_for('symbols'))
    else:
        flash('Login Unsuccessful. Please check your credentials', 'danger')
    return render_template('login.html', title='Login')


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been successfully logged out!', 'success')
    return redirect(url_for('symbols'))


# GET METHOD for Search Bar
@app.route('/get_search')
def get_search():
    """
    Route to accept a GET request to perform
    a search
    """
    query = request.args.get('q')
    results = mongo.db.symbols.find(
        {"category_name": {"$regex": query, "$options": 'i'}})
      # Grab the arugments via GET request
    print(query)
    return render_template(
        'search.html',  query=results)  # Pass the results to the view


@app.route("/display_letter/<letter>")
def display_letter(letter):
    """Display links to all words starting with selected letter."""
    return render_template("letter.html",
                           index = mongo.db.symbols.find({
                            "letter": letter}).sort("category_name"),
                           letter=letter,
                           letters=ALPHABET)


@app.route("/display_word/<word>")
def display_word(word):
    """Display full entry details of selected word."""
    return render_template("symbols.html",
                           word=mongo.db.symbols.find_one({
                            "category_name": word}), letters=ALPHABET)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
