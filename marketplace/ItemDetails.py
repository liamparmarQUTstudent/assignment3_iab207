from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from .models import Item, Comment
from .forms import ItemForm, CommentForm, OrderForm
from . import db


#create  blueprint
### bp = Blueprint('ItemDetails', __name__, url_prefix='/ItemDetails')
bp = Blueprint('ItemDetails', __name__)

@bp.route('/<id>')
def show(id):
    #item = get_item()
    item = Item.query.filter_by(id=id).first()
    cform = CommentForm()
    return render_template('ItemDetails/show.html', item=item, form=cform)

@bp.route('/<id>/comment', methods=['GET', 'POST'])
def comment(id):
    item = Item.query.filter_by(id=id).first()
    cform = CommentForm()
    if cform.validate_on_submit():
        comment = Comment(text=cform.text.data, item=item)

        db.session.add(comment)
        db.session.commit()
        print('Your comment has been added', 'success')
    return render_template('ItemDetails/show.html', item=item, form=cform)    


@bp.route('/create',methods=['GET','POST'])
@login_required 
def create():                                    
    print('Method type: ', request.method)
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data,
                    description = form.description.data,
                    image = form.image.data,
                    cost = form.cost.data,
                    stock = form.stock.data,
                    condition = form.condition.data)
   
        db.session.add(item)
        db.session.commit()
        flash('Successfully created new item', 'success')
        return redirect(url_for('item.create'))

    return render_template('ItemDetails/create.html', form=form)

@bp.route('/OrderPage',methods=['GET','POST'])
@login_required 
def order():                                    
    print('Method type: ', request.method)
    form = OrderForm()
    if form.validate_on_submit():
        order = order(fullname=form.name.data,
                      address=form.description.data,
                      postcode=form.postcode.data)
   
        db.session.add(order)
        db.session.commit()
        flash ('Successfully ordered item. Your order is on the way!', 'success')
        return redirect(url_for('item.order'))

    return render_template('ItemDetails/OrderPage.html', form=form)





##############   USE THIS CODE TEMPORARILY - PRE CHECK BEFORE DATABASE ######################
def get_item():
    # creating the description
    lv_desc = """Slender by name, slender by nature. This wallet in masculine Monogram 
    Eclipse canvas is suitably compact and slim, will carry all the essentials and still 
    fit into a front or back pocket with ease.(Louis Vuitton)"""
    # an image location
    image_loc = 'img/WalletItem2.jpg'
    item = Item('Louis Vuitton', lv_desc, image_loc, 'Price: AU $300', 'More than 10 avaliable', 'BRAND NEW')
    
    # a comment

    comment = Comment(
        "User1", "Great Wallet", '2019-11-12 11:00:00')
    comment2 = Comment(
        "User2", "Great Wallet, would recommend. Fast Delivery. Got it last Monday and has been my favorite wallet.", '2019-11-13 11:00:00')

    item.set_comments(comment)
    item.set_comments(comment2)

    return item