import os
from flask import Flask, render_template, redirect, request, url_for, flash, redirect
from account import RegistrationForm, LoginForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
app = Flask(__name__)

app.config['SECRET_KEY'] = '86f701f1c759b716b1c4e0cb0e4c19fe'


app.config["MONGO_DBNAME"] = 'symbols'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@my1stcluster-phyn3.mongodb.net/symbols?retryWrites=true&w=majority'
# os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", categories=mongo.db.categories.find(), tasks=mongo.db.tasks.find())


@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", title="Tasks",
                           tasks=mongo.db.tasks.find())


@app.route('/add_task')
def add_task():
    return render_template('addtask.html', title="New Tasks",
                           categories=mongo.db.categories.find())


@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))

# edits properties
@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edittask.html', task=the_task, categories=all_categories)


@app.route('/update_task/<task_id>', methods=["POST"])
def update_task(task_id):
    tasks = mongo.db.tasks
    tasks.update({'_id': ObjectId(task_id)}, {
        'task_name': request.form.get('task_name'),
        'category_name': request.form.get('category_name'),
        'task_description': request.form.get('task_description')
    })
    return redirect(url_for('get_tasks'))


@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('get_tasks'))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html', title="Manage Categories", categories=mongo.db.categories.find())


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


# this code is linked to account.py and lets user to register their details to use website
# add methods to actually receive registration data
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # validates if data has been received after form was filled and sent
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        # after form was sent and message of success received user will be redirected to
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

# this code is linked to account.py and lets user to login into website
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # validates if entered data is correct
    if form.validate_on_submit():
        if form.email.data == 'es@es.lv' and form.password.data == 'pw':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
