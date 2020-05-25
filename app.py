import os
from flask import Flask, flash, render_template, redirect, request, url_for, request, session
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'project'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@my1stcluster-phyn3.mongodb.net/project?retryWrites=true&w=majority'
app.config['SECRET_KEY'] = '57ffea7681cec524fff700193e5cdc11'

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",)


@app.route('/symbols')
def symbols():
    return render_template("symbols.html", symbols = mongo.db.symbols.find().sort('symbol_name'))


@app.route('/add_symbol')
def add_symbol():
    return render_template('add_symbol.html')


@app.route('/insert_symbol', methods=['GET', 'POST'])
def insert_symbol():
    symbol = request.form['category_name'].upper()
    symbol_name = request.form['symbol_name'].upper()
    symbol_description = request.form['symbol_description']
    symbol_img = request.form['symbol_img']
    symbols = mongo.db.symbols
    symbols.insert_one({
            'category_name': symbol,
            'symbol_name': symbol_name,
            'symbol_img': symbol_img,
            'symbol_description': symbol_description
        })
    flash(('"{}" has been successfully added to').format(symbol_name), 'success')
    flash(('{}!').format(symbol), 'info')
    return redirect(url_for('symbols',symbol=symbol))


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
        'symbol_name':request.form.get('symbol_name'),
        'symbol_img': request.form.get('symbol_img'),
        'symbol_description': request.form.get('symbol_description')
    })
    return redirect(url_for('symbols'))


@app.route('/delete_symbol/<symbol_id>')
def delete_symbol(symbol_id):
    mongo.db.symbols.remove({'_id': ObjectId(symbol_id)})
    flash(('"{}" has been successfully deleted').format(symbol_id), 'success')
    return redirect(url_for('symbols'))


@app.route('/categories')
def categories():
    return render_template('categories.html', categories=mongo.db.symbols.distinct("category_name"))


@app.route('/register')
def register_page():
    # Generates Register Page
    return render_template('register.html', title='Register')


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})
        # checks if user is in db if not creates new user, if it is starts else
        if existing_user is None:
            # hashes pasword
            hash_password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            #creates new user with hashed pasword
            users.insert({
                'username': request.form['username'],
                'password': hash_password
                })
            flash('Your account has been created successfuly! You can now Login!', 'success')
            return redirect(url_for('login'))
        else:
            flash('This username is already taken! Please try a different username!', 'danger')
        return render_template('register.html')


@app.route('/login')
def login_page():
    # Generates Login Page
    return render_template('login.html', title='Login')


@app.route('/login', methods=["POST", "GET"])
def login():
    users = mongo.db.users
    login_user = users.find_one({'username': request.form['username']})
    # Check for user in db
    if login_user and bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            # logs user in session
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
    return redirect(url_for('index'))


@app.route('/get_search')
def get_search():
    query = request.args.get('search')
    results = mongo.db.symbols.find({"category_name": {"$regex": query, "$options": 'i'}})
    print(query)
    print(results)
    return render_template('search.html', query=list(results))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
