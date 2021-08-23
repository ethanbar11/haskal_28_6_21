# Importing the web library
from flask import Flask

# Creating an object of type flask and starting to run server.
app = Flask(__name__)


#
@app.route('/')
def hello_world():
    return 'Hello World!blalakrklg'


@app.route('/get_snake/<snake_name>')
def get_snake(snake_name):
    return 'My snake name is : {}'.format(snake_name)


if __name__ == '__main__':
    app.run()
