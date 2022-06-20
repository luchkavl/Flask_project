from database_utils.db_connection import DatabaseConnection


def create_blogs_table():
    with DatabaseConnection() as conn:
        cur = conn.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS posts(post_id int primary key, title text, content text)")


def add_post(post_id, title, content):
    with DatabaseConnection() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO posts VALUES(?, ?, ?)", (post_id, title, content))


def get_all_posts() -> dict:
    with DatabaseConnection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM posts")
        posts_content = [{'post_id': post[0], 'title': post[1], 'content': post[2]} for post in cur.fetchall()]
        posts_ids = [post['post_id'] for post in posts_content]
        posts = dict(zip(posts_ids, posts_content))
        return posts

