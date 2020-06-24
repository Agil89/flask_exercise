from flask import Blueprint,render_template,request,redirect,flash,session
from blog.core.models import create_blog,all_blogs,search_blog,blog_info,update_blog,delete_blog
from blog.core.forms import BlogForm
from blog.core.utils import login_required

core = Blueprint(__name__,'core')

@core.route('/')
def home():
    blogs=all_blogs()
    data = request.args.get('search_word')
    if data:
        blogs=search_blog(data)
    context = {
        'blogs': blogs
    }
    return render_template('core/home.html',**context)

@core.route('/create',methods=['GET','POST'])
@login_required
def create():
    form = BlogForm()
    if form.validate_on_submit():
        create_blog(**form.data,image='')
        return redirect('/')
    context= {
        'form': form
    }
    return render_template('core/create.html',**context)

@core.route('/blog/<int:blog_id>')
def blog_function(blog_id):
    blogs_info=blog_info(blog_id)
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
