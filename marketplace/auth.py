from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from .forms import LoginForm, RegisterForm, SellerForm, OrderForm, ItemForm
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .models import User


bp = Blueprint('auth', __name__)

app = Flask =(__name__)

@bp.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    error=None
    if(login_form.validate_on_submit()==True):
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(name=user_name).first()

        if u1 is None:
            error='Incorrect user name'
        elif not check_password_hash(u1.password_hash, password): 
            error='Incorrect password'
        if error is None:
            login_user(u1)
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('user.html', form=login_form, heading='Login')

@bp.route('/register', methods=['GET','POST'])
def register():
    register = RegisterForm()
    if (register.validate_on_submit() == True):
            uname =register.user_name.data
            pwd = register.password.data
            email=register.email_id.data
            u1 = User.query.filter_by(name=uname).first()
            if u1:
                flash('User name already exists, please login')
                return redirect(url_for('auth.login'))
            pwd_hash = generate_password_hash(pwd)
            new_user = User(name=uname, password_hash=pwd_hash, emailid=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('main.index'))
    else:
        return render_template('user.html', form=register, heading='Register as Buyer')


@bp.route('/seller', methods=['GET','POST'])
def seller():
    seller = SellerForm()
    if (seller.validate_on_submit() == True):
            uname = seller.user_name.data
            pwd = seller.password.data
            email=seller.email_id.data
            u1 = User.query.filter_by(name=uname).first()
            if u1:
                flash('User name already exists, please login')
                return redirect(url_for('auth.login'))
            pwd_hash = generate_password_hash(pwd)
            new_user = User(name=uname, password_hash=pwd_hash, emailid=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('main.index'))
    else:
        return render_template('user.html', form=seller, heading='Register as Seller')



@bp.route('/Order', methods=['GET','POST']) 
def order_item():                                  
    order = OrderForm()
    if order.validate_on_submit():
        order = order (fullname=order.fullname.data, 
                       address=order.address.data, 
                       postcode=order.postcode.data)
        db.session.add(order)
        db.session.commit()
        flash('Successfully Purchased Product Order: #4423', 'success') 
    return render_template("ItemDetails\OrderPage.html", order=order)

 
@bp.route('/CreateItem',methods=['GET','POST']) 
def create_item():                                  
    itemform = ItemForm()
    if itemform.validate_on_submit():
        flash ('Uploaded Item', 'success')    
    return render_template("ItemDetails/create.html", itemform=itemform)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))