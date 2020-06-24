from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,ValidationError
from wtforms.validators import DataRequired,Length, Email
from blog.auth.models import check_username,check_email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Length(2, 50), DataRequired()])
    password = PasswordField('Password', validators=[Length(min=8, max=40), DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[Length(2,50),DataRequired()])
    email = StringField('Email', validators=[Email(),Length(max=40), DataRequired()])
    first_name = StringField('Firstname', validators=[Length(max=40), DataRequired()])
    last_name = StringField('Lastname', validators=[Length(max=40), DataRequired()])
    password = PasswordField('Password',validators=[Length(min=8,max=40),DataRequired()])

    def validate_username(self,field):
        if check_username(field.data):
            raise ValidationError('Username already taken')
        return field
    def validate_email(self,field):
        if check_email(field.data):
            raise ValidationError('Email already taken')
        return field
    def validate_password(self,field):
        cap_letter = [letter for letter in field.data if 65 <= ord(letter) <=90]
        if field.data.isdigit():
            raise ValidationError('Enter at least one the letter.')
        elif not cap_letter:
            raise ValidationError('Type at least one title letter.')
        return field