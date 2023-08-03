#!/usr/bin/python3
"""
    Flask application for Axist
"""
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flasgger import Swagger
from os import environ, getenv
from api.v1 import auth
from flask_jwt_extended import JWTManager
from models import storage


app = Flask(__name__)
bcyrpt = Bcrypt(app)
app.config['SECRET_KEY'] = getenv("AXIST_KEY")
app.register_blueprint(auth)
CORS(app)
jwt = JWTManager(app)


@app.teardown_appcontext
def close_dbsession(error):
    """ close storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    404 Error response:
        resource not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


app.config['SWAGGER'] = {
    'title': 'Axist RESTFUL API'
    }

Swagger(app)


if __name__ == "__main__":
    host = environ.get('AXIST_MYSQL_HOST', '0.0.0.0')
    port = int(environ.get('AXIST_MYSQL_PORT', "5000"))
    app.run(host=host, port=port, debug=True)
