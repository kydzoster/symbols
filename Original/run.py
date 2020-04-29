import os
from flaskblog import create_app

app = create_app()

# lets you run code in debug mode
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
