from flask import Blueprint

dict_cmp_accord = Blueprint("dict_cmp_accord", __name__)

from . import views, forms
