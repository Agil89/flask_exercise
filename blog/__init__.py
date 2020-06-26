from flask import Flask,session
from blog.auth.models import get_user,get_user_count
from blog.core.models import get_blog_user_details,get_blog_count,get_info
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_url_path = '/home')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@127.0.0.1:3306/blog_project'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    subject = db.Column(db.String(255),nullable=False)
    message = db.Column(db.Text(),nullable=False)

    def __repr__(self):
        return self.username

class AboutWebsite(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    facebook = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.Integer,nullable=False)


db.create_all()
from blog.auth.controllers import auth
from blog.core.controllers import core

@app.context_processor
def utility_processor():
    def current_user():
        user_id = session.get('user_id')
        if user_id:
            return get_user(user_id)
        else:
            return "Anonymous"
    return dict(current_user=current_user())

@app.context_processor
def utility_processor():
    def get_blog_user(blog_id):
        user_detail = get_blog_user_details(blog_id)
        print(user_detail)
        return f"{user_detail['first_name']} {user_detail['last_name']}"
    return dict(get_blog_user=get_blog_user)

@app.context_processor
def utility_processor():
    def count_of_blogs():
        count = get_blog_count()
        return count
    return dict(count_of_blogs=count_of_blogs())

@app.context_processor
def utility_processor():
    def count_of_users():
        users_count = get_user_count()
        return users_count
    return dict(count_of_users=count_of_users())
app.register_blueprint(auth)
app.register_blueprint(core)

@app.context_processor
def utility_processor():
    def info_about():
        info = get_info()
        return info
    return dict(info_about=info_about())