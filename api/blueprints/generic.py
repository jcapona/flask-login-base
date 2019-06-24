from flask import Blueprint
from api.models.base import db

generic = Blueprint('generic', __name__)

@generic.route('/')
def index():
    return '/'

