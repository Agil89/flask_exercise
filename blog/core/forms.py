from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired,Length


class BlogForm(FlaskForm):
    title = StringField('Title',validators=[Length(min=3,max=255,message='En az 3 en cox 255 xarakter olmalidi'),DataRequired()])
    description = TextAreaField('Description', validators=[Length(min=3), DataRequired()])
    owner_name = StringField('Owner', validators=[Length(min=3, max=50,message='En az 3 en cox 50 xarakter olmalidi'), DataRequired()])