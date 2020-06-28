from flask import Flask,session,send_from_directory
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__,static_url_path = '/home')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@127.0.0.1:3306/blog_project_orm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

BASE_DIRS =os.path.dirname(os.path.abspath(__file__))

UPLOADED_FILES_DIR = os.path.join(BASE_DIRS,'media')
MEDIA_URL = 'media'
if not os.path.isdir(UPLOADED_FILES_DIR):
    os.mkdir(UPLOADED_FILES_DIR)
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOADED_FILES_DIR,filename)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'blog.auth.controllers.sign_in'
from blog.auth.controllers import auth
from blog.core.controllers import core

app.register_blueprint(auth)
app.register_blueprint(core)
#
# from blog.auth.models import get_user,get_user_count
# from blog.core.models import get_blog_user_details,get_blog_count,get_info

# @app.context_processor
# def utility_processor():
#     def current_user():
#         user_id = session.get('user_id')
#         if user_id:
#             return get_user(user_id)
#         else:
#             return "Anonymous"
#     return dict(current_user=current_user())
#
# @app.context_processor
# def utility_processor():
#     def get_blog_user(blog_id):
#         user_detail = get_blog_user_details(blog_id)
#         print(user_detail)
#         return f"{user_detail['first_name']} {user_detail['last_name']}"
#     return dict(get_blog_user=get_blog_user)
#
# @app.context_processor
# def utility_processor():
#     def count_of_blogs():
#         count = get_blog_count()
#         return count
#     return dict(count_of_blogs=count_of_blogs())
#
# @app.context_processor
# def utility_processor():
#     def count_of_users():
#         users_count = get_user_count()
#         return users_count
#     return dict(count_of_users=count_of_users())
#
# @app.context_processor
# def utility_processor():
#     def info_about():
#         info = get_info()
#         return info
#     return dict(info_about=info_about())