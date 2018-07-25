import os

from flask import Flask, render_template
from flask_pymongo import PyMongo

project_name = os.getenv('PROJECT_NAME')
app = Flask(__name__)
app.config["MONGO_URI"] = f"mongodb://mongo_{project_name}:27017/{project_name}"
mongo = PyMongo(app)


def get_record(name):
    if not mongo.db[name].find_one():
        initial_data = {
            'user': '',
            'score': '',
            'money': 0
        }
        mongo.db[name].insert_one(initial_data)
    record = mongo.db[name].find_one()
    return record


@app.route('/user')
@app.route('/score')
@app.route('/money')
def publisher():
    return "Start publishing"


@app.route('/')
def index():
    record = get_record(project_name)
    data = {
        'name': project_name,
        'record': record
    }
    return render_template("index.html", **data)


if __name__ == '__main__':
    app.run()
