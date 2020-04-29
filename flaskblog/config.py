import os

class Config:
    SECRET_KEY = 'a521dc38df3cfadbef1f28d4bd120588'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MONGO_DBNAME = 'symbols'
    MONGO_URI = 'mongodb+srv://root:r00tUser@my1stcluster-phyn3.mongodb.net/symbols?retryWrites=true&w=majority'
