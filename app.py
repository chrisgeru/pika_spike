import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return f"Hello World for Project {os.getenv('PROJECT_NAME')}!"


if __name__ == '__main__':
    app.run()
