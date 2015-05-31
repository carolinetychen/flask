from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import Required, Email


class LoginForm(Form):
    name = StringField('Name', validators=[Required()])
    account = StringField('Account', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Login')


class BoardForm(Form):
    text = IntegerField('Text', validators=[Required()])
    share = SubmitField('Share')
