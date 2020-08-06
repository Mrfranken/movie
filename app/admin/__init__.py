# -*- coding: utf-8 -*-
from flask import Blueprint

admin = Blueprint('admin', __name__)
from .views import user
from .views import views
