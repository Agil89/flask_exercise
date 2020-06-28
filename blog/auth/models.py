# import pymysql.cursors
from blog import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id= db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(40),nullable=False)
    email = db.Column(db.String(40),nullable=False)
    first_name = db.Column(db.String(40),nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    password_hash = db.Column(db.String(255),nullable=False)
    is_active = db.Column(db.Boolean(),default=True,nullable=False)
    is_superuser = db.Column(db.Boolean(),default=False,nullable=False)
    date_joined= db.Column(db.DateTime(timezone=True),server_default=func.now())

    blogs = db.relationship("Blog",backref="user")

    def __init__(self,username,email,first_name,last_name,password):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

db.create_all()

































# connection = pymysql.connect(host='localhost',
#                              user ='root',
#                              password='123',
#                              db='blog_project',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
#
# def create_user_table():
#     with connection.cursor() as cursor:
#             sql = """Create table if not exists users(
#                     id int(11) unsigned AUTO_INCREMENT PRIMARY KEY,
#                     username varchar(50) UNIQUE NOT NULL,
#                     email varchar(50) UNIQUE NOT NULL,
#                     first_name varchar(50) NOT NULL,
#                     last_name varchar(50) NOT NULL,
#                     password varchar(255) NOT NULL,
#                     date_joined datetime NOT NULL,
#                     is_active tinyint(1) DEFAULT 1,
#                     INDEX (id,username)
#                     )"""
#             cursor.execute(sql)
#     connection.commit()
# create_user_table()
#
# def create_user(username,email,first_name,last_name,password,is_active=1,**kwargs):
#     hashed_pass = generate_password_hash(password)
#     with connection.cursor() as cursor:
#             sql = """INSERT INTO blog_project.users(username,email,first_name,last_name,password,date_joined,is_active) VALUES
#             (%s,%s,%s,%s,%s,%s,%s)"""
#             date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#             cursor.execute(sql,(username,email,first_name,last_name,hashed_pass,date,is_active))
#     connection.commit()
#
# def check_username(username):
#     finded_user = None
#     with connection.cursor() as cursor:
#         sql = """select * from blog_project.users where users.username = %s"""
#         cursor.execute(sql,username)
#     finded_user = cursor.fetchone()
#     return finded_user
#
# def check_email(email):
#     finded_email = None
#     with connection.cursor() as cursor:
#         sql = """select * from blog_project.users where users.email = %s"""
#         cursor.execute(sql,email)
#     finded_email = cursor.fetchone()
#     return finded_email
#
# def check_user(username,password):
#     finded_user = None
#     user=check_username(username)
#     if user:
#         pwhash = user['password']
#         if check_password_hash(pwhash,password):
#             finded_user=user
#     return finded_user
#
# def get_user(user_id):
#     finded_user = None
#     with connection.cursor() as cursor:
#         sql = """select * from blog_project.users where users.id = %s"""
#         cursor.execute(sql,user_id)
#     finded_user = cursor.fetchone()
#     return finded_user
#
#
# def get_user_count():
#     with connection.cursor() as cursor:
#         sql = """select count(id) from users"""
#         cursor.execute(sql)
#         return cursor.fetchone()['count(id)']