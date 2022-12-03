
from flask import Blueprint, render_template, request

from utils import get_posts_all, get_comments_by_post_id, get_post_by_pk, search_for_posts, get_posts_by_user

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
def page_index():
    all_posts = get_posts_all()
    return render_template("index.html", posts=all_posts)


@main_blueprint.route('/posts/<int:postid>')
def page_post(postid):
    found_post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template("post.html", post=found_post, comments=comments)


@main_blueprint.route('/search', methods=['GET'])
def search():

    search_query = request.args.get('s')
    posts = search_for_posts(search_query)
    return render_template('search.html', posts=posts)


@main_blueprint.route('/users/<username>', methods=['GET'])
def page_user_feed(username):
    user_posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=user_posts, username=username)
