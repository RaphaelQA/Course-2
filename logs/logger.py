import logging

logger_api_posts = logging.Logger("api_posts")
logger_api_post = logging.Logger("api_post_by_id")

file_hander = logging.FileHandler("logs/api.log")
formatter_api = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_hander.setFormatter(formatter_api)

logger_api_posts.addHandler(file_hander)
logger_api_post.addHandler(file_hander)

logger_api_post.setLevel(logging.INFO)
logger_api_posts.setLevel(logging.INFO)

