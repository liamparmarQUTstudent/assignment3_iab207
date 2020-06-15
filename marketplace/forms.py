from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField 
from wtforms.validators import InputRequired, Length, Email, EqualTo

#add the typesof files allowed as a set
ALLOWED_FILE= { 'jpg', 'JPG'}

class LoginForm(FlaskForm):
    user_name=StringField("Username", validators=[
        InputRequired('Enter Username')])
    password = PasswordField("Password", validators=[
        InputRequired('Enter password')])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    user_name = StringField("Username", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[InputRequired()])
    phone_number = StringField("Phone Number", validators=[InputRequired()])
    password = PasswordField("Password", validators=[
        InputRequired(),
        EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    submit = SubmitField("Register")

class SellerForm(FlaskForm):
    user_name = StringField("Username", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[InputRequired()])
    phone_number = StringField("Phone Number", validators=[InputRequired()])
    bank_number = StringField("Bank Number", validators=[InputRequired()])
    password = PasswordField("Password", validators=[
        InputRequired(),
        EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    submit = SubmitField("Register")

class OrderForm(FlaskForm):
    fullname=StringField("Username", validators=[InputRequired('Enter Fullname')])
    address = StringField("Address", validators=[ InputRequired('Enter Address')])
    postcode = StringField('Postcode',validators=[InputRequired(), Length(max=4)] )
    submit = SubmitField("Order")


class ItemForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = StringField('Cover Image', validators=[InputRequired()])
    cost = StringField('Cost', validators=[InputRequired()])
    stock = StringField('Quantity', validators=[InputRequired()])
    condition = StringField('Condition', validators=[InputRequired()])
    submit = SubmitField('Create')

class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')