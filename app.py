import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'symbols'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@my1stcluster-phyn3.mongodb.net/symbols?retryWrites=true&w=majority'

mongo = PyMongo(app)


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWYZ"

DB = mongo.db


@app.route('/')
@app.route('/get_index')
def get_index():
    return render_template("index.html", letters=ALPHABET)

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
        'category_name': request.form.get('category_name'),
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
    return render_template('categories.html', categories=mongo.db.categories.find())


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
##########################


@app.route("/display_letter/<letter>")
def display_letter(letter):
    """Display links to all words starting with selected letter."""
    return render_template("letter.html",
                           index=DB.entries.find({
                            "letter": letter}).sort("term"),
                           letter=letter,
                           letters=ALPHABET)


@app.route("/find_words", methods=["GET", "POST"])
def find_words():
    """Find and display word(s) matching a searchbox query."""
    entries = DB.entries
    all_entries = entries.find()
    # list comprehension method obtained from datacamp.com
    all_words = [item["term"] for item in all_entries]

    search_term = request.form["search"].lower()

    matches = []

    for entry in all_words:
        if search_term and entry[0:len(search_term)] == search_term:
            matches.append(entry)

    return render_template("search.html", letters=ALPHABET,
                           matches=matches, search_term=search_term)


@app.route("/display_word/<word>")
def display_word(word):
    """Display full entry details of selected word."""
    return render_template("word.html",
                           word=DB.entries.find_one({
                            "term": word}), letters=ALPHABET)


@app.route("/add_word")
def add_word():
    """Display form for adding new word."""
    return render_template("addword.html", letters=ALPHABET)


@app.route("/insert_word", methods=["GET", "POST"])
def insert_word():
    """Process addword form and insert word into DB."""
    word = request.form["term"].lower()
    entries = DB.entries
    all_entries = DB.entries.find()
    all_words = [entry["term"] for entry in all_entries]
    glossary = [item.lower() for item in all_words]

    meanings = []

    # check if first character is a letter
    if word[0].upper() not in ALPHABET:
        flash("A word must start with a letter (English only).")
        return redirect(url_for("add_word"))

    # key-value iteration code obtained from W3Schools.com
    for k, v in request.form.items():
        if k != "term":
            if v != "":
                meanings.append(v)
    # check if same word already exists in DB
    if word.lower() in glossary:
        flash(("Entry '{}' already exists.").format(word))
        return redirect(url_for("add_word"))
    else:
        entries.insert_one(
            {
                "term": word,
                "letter": word[0].upper(),
                "meanings": meanings
            })
        flash(("Entry '{}' successfully added.").format(word))
        return redirect(url_for("display_word", word=word))


@app.route("/edit_word/<word_id>")
def edit_word(word_id):
    """ Display editword form for selected word"""
    word_to_edit = DB.entries.find_one({"_id": ObjectId(word_id)})
    return render_template("editword.html",
                           word=word_to_edit, letters=ALPHABET)


@app.route("/update_word/<word_id>", methods=["GET", "POST"])
def update_word(word_id):
    """Process editword form and insert update(s) into DB"""
    entries = DB.entries
    term_to_update = request.form["term"].lower()
    same_term = entries.find_one({"term": term_to_update})

    meanings = []

    # check if first character is a letter
    if term_to_update[0].upper() not in ALPHABET:
        flash("A word must start with a letter (English only).")
        return redirect(url_for("edit_word",
                                word_id=word_id))
    # key-value iteration code obtained from W3Schools.com
    for k, v in request.form.items():
        if k != "term":
            if v != "":
                meanings.append(v)
    # if word (term) is modified, check if same entry already exists in DB
    if same_term and same_term["_id"] != ObjectId(word_id):
        flash(("Entry '{}' already exists.").format(term_to_update))
        return redirect(url_for("edit_word",
                                word_id=word_id))
    else:
        entries.update_one({"_id": ObjectId(word_id)},
                           {"$set": {
                                "term": term_to_update,
                                "letter": term_to_update[0].upper(),
                                "meanings": meanings
                           }})
    flash("Word successfully updated.")
    return redirect(url_for("display_word",
                            word=term_to_update))


@app.route("/delete_word/<word_id>")
def delete_word(word_id):
    """Delete selected entry from DB."""
    entries = DB.entries
    entries.delete_one({"_id": ObjectId(word_id)})
    flash("Entry successfully deleted.")
    return render_template("addword.html", letters=ALPHABET)


@app.route("/contribute", methods=["GET", "POST"])
def contribute():
    return render_template("contribute.html", letters=ALPHABET)



##########################
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
