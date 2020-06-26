from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired,Length, Email


class BlogForm(FlaskForm):
    title = StringField('Title',validators=[Length(min=3,max=255,message='En az 3 en cox 255 xarakter olmalidi'),DataRequired()])
    description = TextAreaField('Description', validators=[Length(min=3), DataRequired()])
    # owner_name = StringField('Owner', validators=[Length(min=3, max=50,message='En az 3 en cox 50 xarakter olmalidi'), DataRequired()])


class ContactForm(FlaskForm):
    username = StringField('Username',validators=[Length(min=3,max=40,message='40 dan cox simvol olmaz!'),DataRequired()])
    email = StringField('Email', validators=[Email(),Length(min=3,max=40), DataRequired()])
    subject = StringField('Subject',validators=[Length(min=3,max=40,message='40 dan cox simvol olmaz!'),DataRequired()])
    message = TextAreaField(validators=[DataRequired()])

# class AboutWebsiteForm(FlaskForm):
#     facebook = StringField('Facebook',validators=[Length(min=3, max=40), DataRequired()])
#     email = StringField('Email', validators=[Email(), Length(min=8, max=40), DataRequired()])
#     phone =IntegerField('Phone Number',validators=[Length(min=8, max=40), DataRequired()])










