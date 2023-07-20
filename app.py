"""
This module provides a Flask API for fetching users from Firebase Authentication.
"""

from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, auth
from flask_cors import CORS

app = Flask(__name__)
cred = credentials.Certificate("/Users/turhtk222/Desktop/mongoDB_test/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

CORS(app, origins='http://localhost:3002')

@app.route('/')
def hello_world():
    """
    Returns a simple greeting message.
    """
    return 'Hello, World!'

@app.route('/api/users')
def fetch_users():
    """
    Fetches users from Firebase Authentication and returns them as JSON.
    """
    try:
        user_list = auth.list_users()
        fetched_users = [serialize_user(user) for user in user_list.iterate_all()]
        return jsonify(fetched_users)
    except Exception:
        return jsonify({'message': 'Error fetching users'}), 500

def serialize_user(user):
    """
    Serializes a user object to a dictionary.
    """ 
    return {
        'uid': user.uid,
        'email': user.email,
        'displayName': user.display_name
    }

if __name__ == '__main__':
    app.run()
