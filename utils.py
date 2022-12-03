import json

path_posts = 'data/posts.json'
path_com = 'data/comments.json'


def get_posts_all():
    with open(path_posts, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name):
    data = get_posts_all()
    post_user = []
    low_user_name = user_name.lower()
    for post in data:
        try:
            if low_user_name == post['poster_name'].lower():
                post_user.append(post)
        except ValueError:
            return print("Такого пользователя нет")
    return post_user


def get_comments_by_post_id(post_id):
    with open(path_com, 'r', encoding='utf-8') as file:
        comments = json.load(file)
    com_add = []
    for com in comments:
        if post_id == com['post_id']:
            com_add.append(com)
    return com_add


def search_for_posts(query):
    data = get_posts_all()
    low_query = query.lower()
    contents = []
    for word in data:
        if low_query in word["content"].lower().split(" "):
            contents.append(word)
    return contents


def get_post_by_pk(pk):
    data = get_posts_all()
    for pk_f in data:
        if pk == pk_f['pk']:
            return pk_f


print(get_posts_by_user("larry"))
