__author__ = 'owner'

from marketplace.forms import *
from wtforms import Form, PasswordField, TextField
from wtforms.validators import Email, EqualTo

class LoginForm(Form):
    email = TextField("email", validators=[Email()])
    password = PasswordField("password")


class RegistrationForm(Form):

    email = TextField("email", validators=[Email()])
    first_name = TextField("First Name", [validators.required(), validators.length(max=10)])
    last_name = TextField("First Name", [validators.required(), validators.length(max=10)])
    prescription_number = TextField("Prescription Number", [validators.required(), validators.length(max=10)])
    password = PasswordField('New Password', [Required(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    phone = TextField("First Name", [validators.required(), validators.length(max=10)])