from flask import Flask, make_response, jsonify, request
from flask.ext.cors import CORS
from flask.ext import restful
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps


app = Flask(__name__, instance_path='/Users/Linehan/desktop/workspace/capstone/project/instance')
CORS(app, resources=r'/*', allow_headers='Content-Type')
app.config.from_pyfile('config.py')

MONGO_URL = app.config['MONGOLAB_URI']
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/capstone"

client = MongoClient('mongodb://localhost:27017/')
db = client['capstone']
events_collection = db['events']
print dumps(events_collection.find())


posts = [
    {
        "_id": 1,
        "title": "West Parking Lot",
        "body": "Absolute rager out here",
        "time": "5:30pm",
        "upvotes": 8,
        "downvotes": 3,
        "event_id": 1,
        "user": {
            "name": "Sam",
            "favorites": []
        }
    }
]

events = [
    {
        "_id": 1,
        "name": "Fare Thee Well",
        "date": "07/03/2015",
        "num_posts": 3,
        "venue": {
            "name": "Soldier Field",
            "city": "Chicago",
            "state": "IL"
        }
    },
        {
            "_id": 2,
            "name": "Dead & Company",
            "date": "11/25/2015",
            "num_posts": 6,
            "venue": {
                "name": "First Bank Center",
                "city": "Broomfield",
                "state": "CO"
            }
        }
]


@app.route('/posts')
def get_posts():
    return jsonify({'posts': posts})

@app.route('/events')
def get_events():
    return dumps(events_collection.find())


@app.route('/create_event', methods=['POST'])
def create_event():
    form_data = request.data
    print form_data


if __name__ == "__main__":
    app.run(debug=True)
