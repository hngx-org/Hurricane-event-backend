from flask import Blueprint, redirect, url_for, jsonify, request
import os
auth = Blueprint('auth', __name__)
auth.config['SECRET_KEY'] = os.environ.get('key') #Secret key variable name
from auth import routes
