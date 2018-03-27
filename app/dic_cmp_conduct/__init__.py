from flask import Blueprint

dict_cmp_conduct = Blueprint("dict_cmp_conduct", __name__)

from . import views, forms
