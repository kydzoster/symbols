from flask import render_template, url_for, flash, redirect, request, session
from symbols import app, bcrypt
from symbols.forms import RegistrationForm, LoginForm
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
mongo = PyMongo(app)
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DB = mongo.db

posts = [
    {
        'author': 'Martin Silins',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 01, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 01, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register')  # For the register button
def open_register():
    return render_template('register.html', title='Register')


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
    return render_template('login.html', title='Login')


@app.route('/login', methods=["POST", "GET"])
def login():
    users = mongo.db.users
    login_user = users.find_one({'username': request.form['username']})
    if login_user and bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check your credentials', 'danger')
    return render_template('login.html', title='Login')


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been successfully logged out!', 'success')
    return redirect(url_for('home'))


@app.route('/symbols')
def symbols():
    return render_template("symbols.html", symbols=mongo.db.symbols.find())


@app.route('/add_symbol')
def add_symbol():
    return render_template('add_symbol.html',
    # This line will find all Countries in MongoDB
    categories=mongo.db.categories.find())

# This function will deliver inserted data to MongoDB
@app.route('/insert_symbol', methods=['POST'])
def insert_symbol():
    categories = mongo.db.categories
    category_doc = {'category_name': request.form.get('category_name')}
    categories.insert_one(category_doc)
    symbols = mongo.db.symbols
    # this line will insert one form into MongoDB as a dictionary
    symbols.insert_one(request.form.to_dict())
    # this line after submiting will return to symbols.html
    return redirect(url_for('symbols'))


# This function will find properties for symbols by its id with the help of ObjectId
@app.route('/edit_symbol/<symbol_id>')
def edit_symbol(symbol_id):
    the_symbol = mongo.db.symbols.find_one({'_id': ObjectId(symbol_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_symbol.html', symbol=the_symbol, categories=all_categories)


@app.route('/update_symbol/<symbol_id>', methods=["POST"])
def update_symbol(symbol_id):
    symbols = mongo.db.symbols
    symbols.update({'_id': ObjectId(symbol_id)},
    {
        'category_name':request.form.get('category_name'),
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
    return render_template('categories.html',
    categories=mongo.db.categories.find())


# This function will find properties for countries by its id with the help of ObjectId
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('edit_category.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update({'_id': ObjectId(category_id)},
    {'category_name': request.form.get('category_name')})
    return redirect(url_for('categories'))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('categories'))


@app.route("/find_words", methods=["GET", "POST"])
def find_words():
    """Find and display word(s) matching a searchbox query."""
    all_symbols=mongo.db.symbols.find()
    # list comprehension method obtained from datacamp.com
    all_words = [item["category_name"] for item in all_symbols]

    search_category_name = request.form["search"].lower()

    matches = []

    for entry in all_words:
        if search_category_name and entry[0:len(search_category_name)] == search_category_name:
            matches.append(entry)

    return render_template("categories.html", letters=ALPHABET,
                           matches=matches, search_category_name=search_category_name)


@app.route("/display_letter/<letter>")
def display_letter(letter):
    """Display links to all words starting with selected letter."""
    return render_template("symbols.html",
                           index=mongo.db.symbols.find({
                            "letter": letter}).sort("category_name"),
                           letter=letter,
                           letters=ALPHABET)


@app.route("/display_word/<word>")
def display_word(word):
    """Display full entry details of selected word."""
    return render_template("symbols.html",
                           word=mongo.db.symbols.find_one({
                            "category_name": word}), letters=ALPHABET)