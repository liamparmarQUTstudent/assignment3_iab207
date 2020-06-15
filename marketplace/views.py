from flask import Blueprint, render_template, request, session
from .ItemDetails import Item


mainbp = Blueprint('main', __name__)

@mainbp.route('/') 
def index():
    items = Item.query.all()
    return render_template('index.html',  items=items)
