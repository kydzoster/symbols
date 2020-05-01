from flask import render_template, url_for, flash, redirect
from symbols import app
from symbols.forms import RegistrationForm, LoginForm
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
mongo = PyMongo(app)

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


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