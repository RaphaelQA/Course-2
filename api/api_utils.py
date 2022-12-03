import json


def get_all_posts_api():
    with open('./data/posts.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_post_by_pk_api(pk):
    data = get_all_posts_api()

    for pk_f in data:
        if pk == pk_f['pk']:
            return pk_f
