import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'symbols'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@my1stcluster-phyn3.mongodb.net/symbols?retryWrites=true&w=majority'

mongo = PyMongo(app)

# Home Page
@app.route('/')
@app.route('/get_index')
def get_index():
    return render_template("index.html")

# Add Symbols Page
@app.route("/add_symbols")
def add_symbols():
    return render_template("addsymbols.html",
    countries=mongo.db.countries.find(),
    symbols=mongo.db.symbol.find(),
    description=mongo.db.description.find())


# Insert Symbols using POST
@app.route("/insert_symbol", methods=["POST"])
def insert_symbol():
    symbols = mongo.db.symbols
    new_symbol = request.form.get("word_name")
    # If stmnt to prevent duplicate words
    if words.count_documents({'word_name': new_word}, limit=1) == 0:
    symbols.insert_one(request.form.to_dict())
    return redirect(url_for("all_symbols"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
