from typing import List
from fastapi import APIRouter
from dependencies.dependencies import database_dep
from pydantics.posts import *
from .views import TagView

router = APIRouter(
    tags=["tags"]
)

# Routes for tag operations
@router.post("/tags/", response_model=TagRead)
def create_tag(tag: TagCreate, db = database_dep):
    return TagView(db).create_tag(tag)

@router.get("/tags/{tag_id}", response_model=TagRead)
def get_tag(tag_id: int, db = database_dep):
    return TagView(db).get_tag(tag_id)

@router.get("/tags/", response_model=List[TagRead])
def get_all_tags(db = database_dep):
    return TagView(db).get_all_tags()

@router.put("/tags/{tag_id}", response_model=TagRead)
def update_tag(tag_id: int, tag: TagCreate, db = database_dep):
    return TagView(db).update_tag(tag_id, tag)

@router.delete("/tags/{tag_id}")
def delete_tag(tag_id: int, db = database_dep):
    return TagView(db).delete_tag(tag_id)