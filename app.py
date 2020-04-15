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

##############
@app.route('/get_descs')
def get_descs():
    return render_template("descs.html", descs=mongo.db.descs.find())


@app.route('/add_desc')
def add_desc():
    return render_template('adddesc.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_desc', methods=['POST'])
def insert_desc():
    descs = mongo.db.descs
    descs.insert_one(request.form.to_dict())
    return redirect(url_for('get_descs'))


@app.route('/edit_desc/<desc_id>')
def edit_desc(desc_id):
    the_desc = mongo.db.descs.find_one({"_id": ObjectId(desc_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editdesc.html', desc=the_desc, categories=all_categories)


@app.route('/update_desc/<desc_id>', methods=["POST"])
def update_desc(desc_id):
    descs = mongo.db.descs
    descs.update({'_id': ObjectId(desc_id)}, {
        'desc_name': request.form.get('desc_name'),
        'country_name': request.form.get('country_name'),
        'desc_desc': request.form.get('desc_desc')
    })
    return redirect(url_for('get_descs'))


@app.route('/delete_desc/<desc_id>')
def delete_desc(desc_id):
    mongo.db.descs.remove({'_id': ObjectId(desc_id)})
    return redirect(url_for('get_descs'))

# ##########
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


@app.route('/get_categories')
def get_categories():
    return render_template('countries.html', country=mongo.db.categories.find())


@app.route('/edit_country/<country_id>')
def edit_country(country_id):
    return render_template('editcountry.html',
    country=mongo.db.categories.find_one({'_id': ObjectId(country_id)}))


@app.route('/update_country/<country_id>', methods=['POST'])
def update_country(country_id):
    mongo.db.categories.update(
        {'_id': ObjectId(country_id)},
        {'country_name': request.form.get('country_name')})
    return redirect(url_for('get_categories'))


@app.route('/delete_country/<country_id>')
def delete_country(country_id):
    mongo.db.categories.remove({'_id': ObjectId(country_id)})
    return redirect(url_for('get_categories'))


@app.route('/insert_country', methods=['POST'])
def insert_country():
    country_doc = {'country_name': request.form.get('country_name')}
    mongo.db.categories.insert_one(country_doc)
    return redirect(url_for('get_categories'))


@app.route('/add_country')
def add_country():
    return render_template('addcountry.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
