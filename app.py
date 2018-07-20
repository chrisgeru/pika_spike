import os

from flask import Flask, render_template
from flask_pymongo import PyMongo

PROJECT_CONFIGURATION = {
    'user': {
        'mongo_uri': "mongodb://mongo_user:27017/user"
    },
    'score': {
        'mongo_uri': "mongodb://mongo_score:27017/score"
    },
    'money': {
        'mongo_uri': "mongodb://mongo_money:27017/money"
    }
}
project_name = os.getenv('PROJECT_NAME')
config = PROJECT_CONFIGURATION[project_name]
app = Flask(__name__)
app.config["MONGO_URI"] = config['mongo_uri']
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    if not mongo.db[project_name].find_one():
        initial_data = {
            'user': '',
            'score': '',
            'money': 0
        }
        mongo.db[project_name].insert_one(initial_data)
    record = mongo.db[project_name].find_one()
    data = {
        'name': project_name,
        'record': record
    }
    return render_template("index.html", **data)


if __name__ == '__main__':
    app.run()
