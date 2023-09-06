from flask import Flask, request
import json

from controllers.auth_controller import UserController
from controllers.auth_controller import RegisterController


app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Infocell Blog API"

@app.route("/users")
def user():
    userController = UserController()
    return userController.list()

@app.route("/login", methods=["POST", ])
def login():
    return "login app"


@app.route("/register", methods=["POST", ])
def register():
    raw_data = request.data.decode('utf-8')
    json_data = json.loads(raw_data)
    registerController = RegisterController(json_data)
    return str(registerController.register())