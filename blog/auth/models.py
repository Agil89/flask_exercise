import pymysql.cursors
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
connection = pymysql.connect(host='localhost',
                             user ='root',
                             password='123',
                             db='blog_project',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def create_user_table():
    with connection.cursor() as cursor:
            sql = """Create table if not exists users(
                    id int(11) unsigned AUTO_INCREMENT PRIMARY KEY,
                    username varchar(50) UNIQUE NOT NULL,
                    email varchar(50) UNIQUE NOT NULL,
                    first_name varchar(50) NOT NULL,
                    last_name varchar(50) NOT NULL,
                    password varchar(255) NOT NULL,
                    date_joined datetime NOT NULL,
                    is_active tinyint(1) DEFAULT 1,
                    INDEX (id,username)
                    )"""
            cursor.execute(sql)
    connection.commit()
create_user_table()

def create_user(username,email,first_name,last_name,password,is_active=1,**kwargs):
    hashed_pass = generate_password_hash(password)
    with connection.cursor() as cursor:
            sql = """INSERT INTO blog_project.users(username,email,first_name,last_name,password,date_joined,is_active) VALUES
            (%s,%s,%s,%s,%s,%s,%s)"""
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(sql,(username,email,first_name,last_name,hashed_pass,date,is_active))
    connection.commit()

def check_username(username):
    finded_user = None
    with connection.cursor() as cursor:
        sql = """select * from blog_project.users where users.username = %s"""
        cursor.execute(sql,username)
    finded_user = cursor.fetchone()
    return finded_user

def check_email(email):
    finded_email = None
    with connection.cursor() as cursor:
        sql = """select * from blog_project.users where users.email = %s"""
        cursor.execute(sql,email)
    finded_email = cursor.fetchone()
    return finded_email

def check_user(username,password):
    finded_user = None
    user=check_username(username)
    if user:
        pwhash = user['password']
        if check_password_hash(pwhash,password):
            finded_user=user
    return finded_user

def get_user(user_id):
    finded_user = None
    with connection.cursor() as cursor:
        sql = """select * from blog_project.users where users.id = %s"""
        cursor.execute(sql,user_id)
    finded_user = cursor.fetchone()
    return finded_user


def get_user_count():
    with connection.cursor() as cursor:
        sql = """select count(id) from users"""
        cursor.execute(sql)
        return cursor.fetchone()['count(id)']