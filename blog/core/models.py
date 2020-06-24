import pymysql.cursors
from datetime import datetime
from blog.auth.models import create_user_table
connection = pymysql.connect(host='localhost',
                             user ='root',
                             password='123',
                             db='blog_project1',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def create_blog_table():
    with connection.cursor() as cursor:
            sql = """Create table if not exists blogs(
                    id int(11) unsigned AUTO_INCREMENT PRIMARY KEY,
                    title varchar(255) NOT NULL,
                    description text NOT NULL,
                    owner_name varchar(50) NOT NULL,
                    image varchar(500),
                    created_at datetime NOT NULL,
                    is_published tinyint(1) DEFAULT 1,
                    auth_id int(11),
                    FOREIGN KEY (auth_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
                    INDEX (id,title)
                    )"""
            cursor.execute(sql)
    connection.commit()
create_user_table()
create_blog_table()

def create_blog(title,description,owner_name,image,is_published=True,**kwargs):
    with connection.cursor() as cursor:
        sql = """INSERT INTO blog_project.blogs(title,description,owner_name,image,created_at,is_published)
        VALUES(%s,%s,%s,%s,%s,%s)"""
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(sql,(title,description,owner_name,image,created_at,is_published))
    connection.commit()

def all_blogs():
    with connection.cursor() as cursor:
        sql = """select * from blog_project.blogs"""
        cursor.execute(sql)
    return cursor.fetchall()

def search_blog(search_word):
    with connection.cursor() as cursor:
        sql = """SELECT * from blog_project.blogs WHERE title LIKE %s"""
        cursor.execute(sql, ("%" + search_word + "%",))
    return cursor.fetchall()

def blog_info(id):
    with connection.cursor() as cursor:
        sql = """select * from blog_project.blogs WHERE id=%s"""
        cursor.execute(sql,id)
    return cursor.fetchone()

def update_blog(title,description,owner_name,id,**kwargs):
    with connection.cursor() as cursor:
        sql = """update blog_project.blogs SET title=%s,description=%s,owner_name=%s WHERE id=%s"""
        cursor.execute(sql,(title,description,owner_name,id))
    connection.commit()
    return cursor.fetchone()

def delete_blog(id):
    with connection.cursor() as cursor:
        sql = """delete from blog_project.blogs WHERE id=%s"""
        cursor.execute(sql,id)
    connection.commit()
    return cursor.fetchone()