from flask import Blueprint

tone = Blueprint("tone", __name__)

from . import views, forms