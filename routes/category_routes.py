from typing import List
from fastapi import APIRouter
from dependencies.dependencies import database_dep
from pydantics.posts import *
from .views import CategoryView

router = APIRouter(
    tags=["Category"]
)

@router.post("/categories/", response_model=CategoryRead)
def create_category(category: CategoryCreate, db = database_dep):
    return CategoryView(db).create_category(category)

@router.get("/categories/{category_id}", response_model=CategoryRead)
def get_category(category_id: int, db = database_dep):
    return CategoryView(db).get_category(category_id)

@router.get("/categories/", response_model=List[CategoryRead])
def get_all_categories(db = database_dep):
    return CategoryView(db).get_all_categories()

@router.put("/categories/{category_id}", response_model=CategoryRead)
def update_category(category_id: int, category: CategoryCreate, db = database_dep):
    return CategoryView(db).update_category(category_id, category)

@router.delete("/categories/{category_id}")
def delete_category(category_id: int, db = database_dep):
    return CategoryView(db).delete_category(category_id)