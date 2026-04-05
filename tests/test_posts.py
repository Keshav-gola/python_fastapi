from typing import List
from app import schemas
import pytest


def test_get_all_posts(authenticated_client, test_posts):
    res = authenticated_client.get("/posts/")
    def validate(post):
        return schemas.PostOut(**post)
    posts_map = map(validate, res.json())
    print(list(posts_map))
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    

def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401

def test_unauthorized_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_get_one_post_not_exist(authenticated_client, test_posts):
    res = authenticated_client.get(f"/posts/888888")
    assert res.status_code == 404

def test_get_one_post(authenticated_client, test_posts):
    res = authenticated_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.title == test_posts[0].title
    assert post.Post.content == test_posts[0].content
    assert res.status_code == 200

@pytest.mark.parametrize("title, content, published", [
    ("first title", "first content", True),
    ("second title", "second content", False),
    ("third title", "third content", True),
])
def test_create_post(authenticated_client, test_user, test_posts, title, content, published):
    res = authenticated_client.post("/posts/", json={"title": title, "content": content, "published": published})
    created_post = schemas.Post(**res.json())
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user["id"]
    assert res.status_code == 201

def test_create_post_default_published(authenticated_client, test_user, test_posts):
    res = authenticated_client.post("/posts/", json={"title": "title", "content": "content"})
    created_post = schemas.Post(**res.json())
    assert created_post.published == True
    assert res.status_code == 201