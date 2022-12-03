from flask import jsonify, Blueprint

from api.api_utils import get_post_by_pk_api, get_all_posts_api

from logs.logger import logger_api_posts, logger_api_post

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    logger_api_posts.info("Api запрос постов")
    return jsonify(get_all_posts_api())


@api_blueprint.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post_pk(post_id):
    logger_api_post.info("Api запрос поста")
    return jsonify(get_post_by_pk_api(post_id))
