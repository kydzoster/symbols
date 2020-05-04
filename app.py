import os
from flask import Flask, render_template, redirect, request, url_for, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'project'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@my1stcluster-phyn3.mongodb.net/project?retryWrites=true&w=majority'
app.config['SECRET_KEY'] = '57ffea7681cec524fff700193e5cdc11'
mongo = PyMongo(app)


@app.route('/')
@app.route('/symbols')
def symbols():
    return render_template("symbols.html", symbols=mongo.db.symbols.find())


@app.route('/login')  # For the login Button
def show_login():
    return render_template('login.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    users = mongo.db.users
    login_user = users.find_one({'user_username': request.form['user_username']})  #Check if user info is in the system

    if login_user:
        if bcrypt.hashpw(request.form['user_password'].encode('utf-8'), login_user['user_password']) == login_user['user_password']:
            session['user_username'] = request.form['user_username']
            return redirect(url_for('login'))
    else:
        invalid_user = 'Invalid username/password combination'
    return render_template('login.html', message=invalid_user)


@app.route('/register')  # For the register button
def show_register():
    return render_template('register.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({
            'user_username': request.form['user_username']
            })  # Check if user is in the system
        if existing_user is None:  # If not.. 
            hashpass = bcrypt.hashpw(request.form['user_password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({
                'user_username': request.form['user_username'],   #Insert user info given in the form, into new user object in database
                'user_password': hashpass
                })
            session['user_username'] = request.form['user_username']
            return redirect(url_for('login'))
        else:
            invalid_user = 'This username already exists'
        return render_template('register.html', message=invalid_user)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('symbols'))


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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
