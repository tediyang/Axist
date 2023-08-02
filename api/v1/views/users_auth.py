#!/usr/bin/python3

""" import users module and other neccessary modules"""
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import users


# Initialize JWTManager
jwt = JWTManager()
jwt.init_app(app_users_auth)


# Sample token data to store logged-in users
tokens = {}

# Function to check user credentials
def authenticate(username, password):
    """ Authentication of credentials """
    if username in users and users[username]["password"] == password:
        return True
    return False

# Login endpoint
@user_auth_bp.route('/login', method=['POST'])
def login():
    ''' login defined '''
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Unauthorized. Please provide username and password."}, 400)

    username = data['username']
    password = data['password']

    if authenticate(username, password):
        token = create_access_token(identity=username)
        tokens[token] = username
        return jsonify({"access_token": token}, 200)
    else:
        return jsonify({"message": "Invalid request: input valid username or password."}, 401)

# Logout endpoint
@app_users_auth.route('/logout', method=['POST'])
@jwt_required()
def logout():
    ''' Logout defined '''
    token = request.headers.get('Authorization')
    if token in tokens:
        del tokens[token]
        return jsonify({"message": "Logout successful."}, 200)
    else:
        return jsonify({"message": "Invalid token or token expired."}, 401)
