from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:Hello@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app) 
migrate = Migrate(app, db)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))
    deleted = db.Column(db.Boolean)


    def __init__(self, title):
        self.title = title
        self.deleted = False


@app.route('/')
def index():

    return redirect('/blog')

@app.route('/blog', methods =['POST', 'GET'])
def blog():
    total_blogs = Blog.query.filter_by(deleted=False).all()
    deleted_blogs = Blog.query.filter_by(deleted=True).all()
    return render_template('blog.html', title='Build a Blog!', blogs=total_blogs, deletedBlogs= deleted_blogs)

@app.route('/newpost', methods =['POST', 'GET'])
def newpost():

    if request.method == 'POST':
        blog_title = request.form['blogTitle']
        new_blog = Blog(blog_title)
        blog_body = request.form['blogBody']
        blog_entry = Blog(blog_body)
        
        if blog_title == " " or blog_body == " ":
            title_error = "Successful Title"
            body_error = "Sucessful Body"
            if blog_title == " " and blog_body == " ":
                title_error = "Your blog is missing a title"
                body_error = "Your blog is missing content"   
            elif blog_title == " ":
                title_error= "Your blog is missing a title"
            elif body_body == " ":
                body_error= "your blog is missing content"
        return render_template('newpost.html, title_error = title_error, body_error = body_error')    
        
    else:

        db.session.add(new_blog)
        db.session.add(blog_entry)
        db.session.commit()

        return redirect('/blog')


@app.route('/delete-blog', methods=['POST'])
def delete_blog():

    blog_id = int(request.form['blog-id'])
    blogd = Blog.query.get(blog_id)
    blogd.deleted = True
    db.session.add(blogd)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run()