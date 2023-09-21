from flask import Blueprint

api_views = Blueprint("api_views", __name__)

from views.comment import *
from views.event import *
from views.group import *
from views.user import *
