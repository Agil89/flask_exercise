# import pymysql.cursors
from datetime import datetime
from blog import db
from sqlalchemy.sql import func

class Contact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    subject = db.Column(db.String(255),nullable=False)
    message = db.Column(db.Text(),nullable=False)

    def __repr__(self):
        return self.username

class Blog(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.String(500), nullable=False)
    created_at= db.Column(db.DateTime(timezone=True),server_default=func.now())
    is_published = db.Column(db.Boolean(), default=True, nullable=False)

    def __repr__(self):
        return self.username

class AboutWebsite(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    facebook = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.Integer,nullable=False)

db.create_all()























# connection = pymysql.connect(host='localhost',
#                              user ='root',
#                              password='123',
#                              db='blog_project',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
#
# def create_blog_table():
#     with connection.cursor() as cursor:
#             sql = """Create table if not exists blogs(
#                     id int(11) unsigned AUTO_INCREMENT PRIMARY KEY,
#                     title varchar(255) NOT NULL,
#                     description text NOT NULL,
#                     image varchar(500),
#                     created_at datetime NOT NULL,
#                     auth_id int(11) unsigned NOT NULL,
#                     is_published tinyint(1) DEFAULT 1,
#                     FOREIGN KEY (auth_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
#                     INDEX (id,title)
#                     )"""
#             cursor.execute(sql)
#     connection.commit()
#
# create_blog_table()
#
# def create_blog(title,description,image,auth_id,is_published=True,**kwargs):
#     with connection.cursor() as cursor:
#         sql = """INSERT INTO blog_project.blogs(title,description,image,created_at,auth_id,is_published)
#         VALUES(%s,%s,%s,%s,%s,%s)"""
#         created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         cursor.execute(sql,(title,description,image,created_at,auth_id,is_published))
#     connection.commit()
#
# def all_blogs(limit_f_index=None,limit_s_index=None):
#     limit_query=''
#     if limit_f_index is not None and limit_s_index is not None:
#         limit_query=f"LIMIT {limit_f_index},{limit_s_index}"
#     with connection.cursor() as cursor:
#         sql = f"""select * from blog_project.blogs {limit_query}"""
#         cursor.execute(sql)
#     return cursor.fetchall()
#
# def search_blog(search_word):
#     with connection.cursor() as cursor:
#         sql = """SELECT * from blog_project.blogs WHERE title LIKE %s"""
#         cursor.execute(sql, ("%" + search_word + "%",))
#     return cursor.fetchall()
#
# def blog_info(id):
#     with connection.cursor() as cursor:
#         sql = """select * from blog_project.blogs WHERE id=%s"""
#         cursor.execute(sql,id)
#     return cursor.fetchone()
#
# def update_blog(title,description,owner_name,id,**kwargs):
#     with connection.cursor() as cursor:
#         sql = """update blog_project.blogs SET title=%s,description=%s,owner_name=%s WHERE id=%s"""
#         cursor.execute(sql,(title,description,owner_name,id))
#     connection.commit()
#     return cursor.fetchone()
#
# def delete_blog(id):
#     with connection.cursor() as cursor:
#         sql = """delete from blog_project.blogs WHERE id=%s"""
#         cursor.execute(sql,id)
#     connection.commit()
#     return cursor.fetchone()
#
# def get_blog_user_details(blog_id):
#     with connection.cursor() as cursor:
#         sql = """select users.first_name,users.last_name from blogs
#          INNER JOIN users on users.id = blogs.auth_id where blogs.id=%s"""
#         cursor.execute(sql,blog_id)
#         return cursor.fetchone()
#
# def get_blog_count():
#     with connection.cursor() as cursor:
#         sql = """select count(id) from blogs"""
#         cursor.execute(sql)
#         return cursor.fetchone()['count(id)']
#
# def get_info():
#     with connection.cursor() as cursor:
#         sql = """select * from about_website"""
#         cursor.execute(sql)
#         return cursor.fetchone()