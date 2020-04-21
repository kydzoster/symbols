import os
from flaskblog import app

# lets you run code in localhost and see every change you make in real time made in this file app.py
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
