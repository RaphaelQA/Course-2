import pytest

from utils import *

def test_get_posts_all():
    assert type(get_posts_all()) == list

