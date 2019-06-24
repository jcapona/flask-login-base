from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('Email', 
            validators=[Email("This field requires a valid email address")], 
            render_kw={'placeholder': 'Email', 'type': 'email'})
    password = PasswordField('Password', 
            validators=[InputRequired(), Length(min=4, max=10)], 
            render_kw={'placeholder': 'Password', 'type': 'password'})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    email = StringField('Email', 
            validators=[Email("This field requires a valid email address")], 
            render_kw={'placeholder': 'Email', 'type': 'email'})
    password = PasswordField('Password', 
            validators=[InputRequired(), Length(min=4, max=10)], 
            render_kw={'placeholder': 'Password', 'type': 'password'})
    name = StringField('Name', 
            validators=[InputRequired(), Length(min=5, max=20)], 
            render_kw={'placeholder': 'Name'})
    submit = SubmitField('Sign In')
