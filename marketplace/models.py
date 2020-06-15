from . import db
from datetime import datetime
from flask_login import UserMixin

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(512))
    image = db.Column(db.String(400))
    cost = db.Column(db.Float)
    stock = db.Column(db.Float)
    condition = db.Column(db.String(32))

    # Back Reference for the relationship of comments
    comments = db.relationship('Comment', backref='item')

    def __repr__(self):
        return "<name:{}>".format(self.name)
    
 

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    

    def __repr__(self):
        return "<Comment: {}>".format(self.text)



class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)


    # back reference for relationship of comments
    comments = db.relationship('Comment', backref='user')






class Order(db.Model):
    __tablename__ = 'orders'
    fullname = db.Column(db.String(100), primary_key=True)
    address = db.Column(db.String(100), index=True, nullable=False)
    postcode = db.Column(db.String(100), index=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
   
    def __repr__(self):
        return "<fullname:{}>".format(self.fullname)

    # Back Reference for the relationship of Item
    items = db.relationship('Item', backref='item')



   