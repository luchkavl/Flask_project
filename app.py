from flask import Flask, render_template, request, redirect, url_for
from database_utils.database import get_all_posts, create_blogs_table, add_post

app = Flask(__name__)

create_blogs_table()


@app.route('/')   # homepage
def home():
	posts = get_all_posts()
	return render_template('home.jinja2', posts=posts)   # when user visits homepage this will return to him


@app.route('/post/<int:post_id>')
def post(post_id):
	posts = get_all_posts()
	post = posts.get(post_id)
	if not post:
		return render_template('404.jinja2', message=f'A post with id {post_id} was not found.')
	return render_template('post.jinja2', post=post)


@app.route('/post/create', methods=['GET', 'POST'])
def create_post():
	if request.method == 'POST':
		posts = get_all_posts()
		title = request.form.get('title')
		content = request.form.get('content')
		post_id = len(posts)
		add_post(post_id, title, content)
		return redirect(url_for('post', post_id=post_id))
	return render_template('create.jinja2')


if __name__ == '__main__':
	app.run(debug=True)  # it runs app. debug flag will give us more info if error happens

