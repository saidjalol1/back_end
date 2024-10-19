from pydantic import BaseModel
from typing import List, Optional

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class TagRead(TagBase):
    id: int

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str
    body: str
    image: Optional[str] = None
    category_id: int
    tags: List[int]

class PostCreate(PostBase):
    pass

class PostRead(PostBase):
    id: int
    likes: int
    dislikes: int
    views: int
    category: CategoryRead
    tags: List[TagRead]

    class Config:
        orm_mode = True
