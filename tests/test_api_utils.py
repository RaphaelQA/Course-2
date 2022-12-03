import pytest

from api.api_utils import *


def test_get_all_posts_api():
    assert type(get_all_posts_api()) == list


def test_get_post_by_pk_api():
    for i in range(1, 8):
        assert type(get_post_by_pk_api(i)) == dict


expected_keys = ["poster_name", "poster_avatar", "pic", "content", "views_count",
                 "likes_count", "pk"]


def test_keys_get_all_posts_api():
    for post in get_all_posts_api():
        keys = [key for key in post.keys()]
        assert keys == expected_keys