from flask import Flask


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'project'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@my1stcluster-phyn3.mongodb.net/project?retryWrites=true&w=majority'
app.config['SECRET_KEY'] = '3958a1e4d0ec12d0643fcf1d0b125006'

from symbols import routes