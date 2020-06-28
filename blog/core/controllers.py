from flask import Blueprint,render_template,request,redirect,flash,session
# from blog.core.models import create_blog,all_blogs,search_blog,blog_info,update_blog,delete_blog,get_blog_count
from blog.core.forms import BlogForm,ContactForm
# from blog.core.utils import login_required
from flask_login import login_required,current_user
from blog import db,UPLOADED_FILES_DIR,MEDIA_URL
from blog.core.models import AboutWebsite,Blog
import math

import os
from blog.core.utils import save_file

core = Blueprint(__name__,'core')

@core.route('/')
def home():
    page = int(request.args.get('page',1))
    blogs=Blog.query.filter_by().order_by(Blog.created_at.desc()).limit(2).offset((page-1)*2)
    page_count = math.ceil(Blog.query.filter_by().count()/2)
    page_range = range(1,page_count+1)
    next_page = None
    previous_page = None
    if page+1 <= page_count:
        next_page= page+1
    if page-1 >= 0:
        previous_page= page -1
    data = request.args.get('search_word')
    if data:
        blogs=search_blog(data)
    context = {
        'blogs': blogs,
        'page_range':page_range,
        'next_page':next_page,
        'previous_page':previous_page,
        'current_page':page,
    }
    return render_template('core/home.html',**context)

@core.route('/create',methods=['GET','POST'])
@login_required
def create():
    form = BlogForm()
    if request.method=='POST' and form.validate_on_submit():
        f = form.image.data
        file_path = save_file(f)
        blog= Blog(title=form.title.data,description=form.description.data,image=file_path,user_id=current_user.id)
        # create_blog(**form.data,image='',auth_id=session.get('user_id'))
        db.session.add(blog)
        db.session.commit()
        return redirect('/')
    context= {
        'form': form
    }
    return render_template('core/create.html',**context)

@core.route('/blog/<int:blog_id>')
def blog_function(blog_id):
    blogs_info=blog_info(blog_id)
    print(blogs_info)
    context = {
        'blogs_info':blogs_info
    }
    return render_template('core/blog.html',**context)

@core.route('/update/<int:id>',methods=['GET','POST'])
def change_blog(id):
    if request.method=='GET':
        blogs_info=blog_info(id)
        form = BlogForm(data=blogs_info)
        context = {
            'form': form
        }
        return render_template('core/update.html', **context)
    else:
        form = BlogForm()
        if form.validate_on_submit():
            update_blog(**form.data,id=id)
            flash('Blog updated')
            return redirect('/')

@core.route('/delete/<int:id>')
def remove_blog(id):
    delete_blog(id)
    flash('Blog deleted')
    return redirect('/')

@core.route('/contact',methods=['GET','POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact_info=Contact(username=form.username.data,email=form.email.data,subject = form.subject.data,message=form.message.data)
        db.session.add(contact_info)
        db.session.commit()
        flash('Your message send')
        return redirect('/')
    context = {
        'form':form
    }
    return render_template('core/contact.html',**context)

@core.route('/faqs',methods=['GET','POST'])
def faqs():
    questions = Contact.query.all()
    context = {
        'questions':questions
    }
    return render_template('core/faqs.html',**context)

@core.route('/about',methods=['GET','POST'])
def about():
    about_info=AboutWebsite(facebook='flask_blog/facebook.com',email='myBlog@flask.com',phone =3333333)
    db.session.add(about_info)
    db.session.commit()
    context = {
        'about_info':about_info
        }
    return render_template('core/about.html',**context)
