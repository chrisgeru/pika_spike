import os

from sanic import Sanic
from sanic_mongodb_ext import MongoDbExtension
from umongo import MotorAsyncIOInstance

from trem.views import bp

# Create Sanic App
app = Sanic(__name__)

# Add static folder
app.static('/static', './static')

# Config Mongo
project_name = os.getenv('PROJECT_NAME')
app.config.update({
    "MONGODB_DATABASE": project_name,
    "MONGODB_URI": f"mongodb://mongo_{project_name}:27017",
    "LAZY_UMONGO": MotorAsyncIOInstance(),
})
MongoDbExtension(app)
instance = app.config["LAZY_UMONGO"]

# Config Views from Blueprint
app.blueprint(bp)

def run():
    app.run(host="0.0.0.0", port=5000)
