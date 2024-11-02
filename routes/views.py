from typing import List, Annotated
from fastapi import HTTPException, UploadFile, File, Request, Response, Cookie
from sqlalchemy.orm import Session
from models import Post, Category, Tag 
from pydantics.posts import PostCreate, CategoryCreate, TagCreate


class BlogView:
    def __init__(self, db: Session):
        self.db = db
    # Create a new blog post
    def create_post(self, post: PostCreate):
        category = self.db.query(Category).filter(Category.id == post.category_id).first()
        if not category:
            raise HTTPException(status_code=400, detail="Category not found")

        tags = self.db.query(Tag).filter(Tag.id.in_(post.tags)).all()
        if len(tags) != len(post.tags):
            raise HTTPException(status_code=400, detail="Some tags not found")
         
        new_post = Post(
            title=post.title,
            body=post.body,
            image=post.image,
            category_id=post.category_id,
            tags=tags
        )
        self.db.add(new_post)
        self.db.commit()
        self.db.refresh(new_post)
        return new_post

    # Get a post by ID
    def get_post(self, post_id: int, request, response):
        post = self.db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
         # Check and update the views in the client's browser session
        viewed_posts = request.cookies.get("posts")
        print(viewed_posts)
        if viewed_posts:
            viewed_posts = viewed_posts.split(",")
            print(viewed_posts)
        else:
            viewed_posts = []

        if str(post_id) not in viewed_posts:
            post.views += 1  
            request.cookies.get("posts")
            viewed_posts.append(str(post_id))
            response.set_cookie(key="posts", value=",".join(viewed_posts), samesite="None", secure=True)  # Update cookie with viewed posts
            self.db.commit()
            self.db.refresh(post)
            print(request.cookies.get("posts"))
        else:
            pass
        return post
    def like_post(self, post_id: int, request, response, option):
        post = self.db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
         # Check and update the views in the client's browser session
        liked_posts = request.cookies.get("liked_posts")
        disliked_posts = request.cookies.get("disliked_posts")
        print(liked_posts)
        if liked_posts:
            liked_posts = liked_posts.split(",")
        else:
            liked_posts = []
            
        if disliked_posts:
            disliked_posts = disliked_posts.split(",")
        else:
            disliked_posts = []

        if str(post_id) not in liked_posts and option == "like":
            post.likes += 1  
            if str(post_id) in disliked_posts:
                post.dislikes -= 1
                self.db.commit()
                disliked_posts.remove(str(post_id))
                response.set_cookie(key="disliked_posts", value=",".join(disliked_posts), samesite="None", secure=True)
            liked_posts.append(str(post_id))
            response.set_cookie(key="liked_posts", value=",".join(liked_posts), samesite="None", secure=True)  # Update cookie with viewed posts
            self.db.commit()
            self.db.refresh(post)
            print(request.cookies.get("liked_posts"))
        elif str(post_id) not in disliked_posts and option == "dislike":
            post.dislikes += 1  
            if str(post_id) in liked_posts:
                post.likes -= 1
                self.db.commit()
                liked_posts.remove(str(post_id))
                response.set_cookie(key="liked_posts", value=",".join(liked_posts), samesite="None", secure=True)
            disliked_posts.append(str(post_id))
            response.set_cookie(key="disliked_posts", value=",".join(disliked_posts), samesite="None", secure=True)  # Update cookie with viewed posts
            self.db.commit()
            self.db.refresh(post)
            print(request.cookies.get("disliked_posts"))
        else:
            pass
        return post
    # Get all posts
    def get_all_posts(self):
        return self.db.query(Post).all()

    # Update a post
    def update_post(self, post_id: int, post_data: PostCreate):
        post = self.db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        post.title = post_data.title
        post.body = post_data.body
        post.image = post_data.image
        post.category_id = post_data.category_id
        post.tags = self.db.query(Tag).filter(Tag.id.in_(post_data.tags)).all()

        self.db.commit()
        self.db.refresh(post)
        return post
    
    def delete_post(self, post_id: int):
        post = self.db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        self.db.delete(post)
        self.db.commit()
        return {"message": "Post deleted successfully"}


class CategoryView:
    def __init__(self, db: Session):
        self.db = db

    # Create a new category
    def create_category(self, category: CategoryCreate):
        db_category = self.db.query(Category).filter(Category.name == category.name).first()
        if db_category:
            raise HTTPException(status_code=400, detail="Category already exists")
        
        new_category = Category(name=category.name)
        self.db.add(new_category)
        self.db.commit()
        self.db.refresh(new_category)
        return new_category

    # Get a category by ID
    def get_category(self, category_id: int):
        category = self.db.query(Category).filter(Category.id == category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

    # Get all categories
    def get_all_categories(self):
        return self.db.query(Category).all()

    # Update a category
    def update_category(self, category_id: int, category_data: CategoryCreate):
        category = self.db.query(Category).filter(Category.id == category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

        category.name = category_data.name
        self.db.commit()
        self.db.refresh(category)
        return category

    # Delete a category
    def delete_category(self, category_id: int):
        category = self.db.query(Category).filter(Category.id == category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

        self.db.delete(category)
        self.db.commit()
        return {"message": "Category deleted successfully"}
    

class TagView:
    def __init__(self, db: Session):
        self.db = db

    # Create a new tag
    def create_tag(self, tag: TagCreate):
        db_tag = self.db.query(Tag).filter(Tag.name == tag.name).first()
        if db_tag:
            raise HTTPException(status_code=400, detail="Tag already exists")
        
        new_tag = Tag(name=tag.name)
        self.db.add(new_tag)
        self.db.commit()
        self.db.refresh(new_tag)
        return new_tag

    # Get a tag by ID
    def get_tag(self, tag_id: int):
        tag = self.db.query(Tag).filter(Tag.id == tag_id).first()
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        return tag

    # Get all tags
    def get_all_tags(self):
        return self.db.query(Tag).all()

    # Update a tag
    def update_tag(self, tag_id: int, tag_data: TagCreate):
        tag = self.db.query(Tag).filter(Tag.id == tag_id).first()
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")

        tag.name = tag_data.name
        self.db.commit()
        self.db.refresh(tag)
        return tag

    # Delete a tag
    def delete_tag(self, tag_id: int):
        tag = self.db.query(Tag).filter(Tag.id == tag_id).first()
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")

        self.db.delete(tag)
        self.db.commit()
        return {"message": "Tag deleted successfully"}