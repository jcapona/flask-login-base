from flask import Blueprint, render_template

from api.models.base import db

generic = Blueprint('generic', __name__)


@generic.route('/')
def index():
    return render_template('index.html')

