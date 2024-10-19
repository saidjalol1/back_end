from typing import List
from fastapi import APIRouter
from dependencies.dependencies import database_dep
from pydantics.posts import *
from .views import BlogView

router = APIRouter(
    tags=["Posts"]
)

@router.post("/posts/", response_model=PostRead)
def create_post(post: PostCreate, db = database_dep):
    return BlogView(db).create_post(post)

@router.get("/posts/{post_id}", response_model=PostRead)
def get_post(post_id: int, db = database_dep):
    return BlogView(db).get_post(post_id)

@router.get("/posts/", response_model=List[PostRead])
def get_all_posts(db = database_dep):
    return BlogView(db).get_all_posts()

@router.put("/posts/{post_id}", response_model=PostRead)
def update_post(post_id: int, post: PostCreate, db = database_dep):
    return BlogView(db).update_post(post_id, post)

@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db = database_dep):
    return BlogView(db).delete_post(post_id)
