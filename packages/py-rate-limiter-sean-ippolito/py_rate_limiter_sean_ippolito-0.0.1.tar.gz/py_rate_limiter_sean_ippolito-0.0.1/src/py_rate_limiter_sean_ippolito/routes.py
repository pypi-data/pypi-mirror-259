from flask import Flask, jsonify
import datetime
from db import client

server = Flask(__name__)

# @server.route("/")
# def main():
#     return "<p>Hello, World dddddddd!</p>"

def get_data(data):
     data['_id'] = str(data['_id'])
     return data

@server.route("/")
def main():
    db = client['python_test']

    new_user = {
        "first_name": "Sean",
        "last_name": "Ippolito",
        "email": "ippolitosean@gmail.com",
        "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }

    users = db.users
    existing_user = users.find_one()
    if not existing_user:
        user_id = users.insert_one(new_user).inserted_id
        print(user_id)
    temp = [get_data(existing_user)]
    return jsonify(temp)