from typing import List, Annotated
from fastapi import APIRouter, UploadFile, File, Request, Response, Cookie
from dependencies.dependencies import database_dep, super_user
from pydantics.posts import *
from pydantics.user_models import *
from .google_drive import  upload_image_to_tmp
from .views import BlogView
import smtplib

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'saidjalol1908@gmail.com'
smtp_password = 'thnc gknk rtup snws'
from_email = 'saidjalol1908@gmail.com'
to_email = 'saidjalolturakhujayev@example.com'

subject = 'Media! New Blog came out!!!'
link = "https://posts/1"
body = f'Hi, This is Media again, new blog came out , enjoy reading \n\n {link}'

router = APIRouter(
    tags=["Posts"]
)


# @router.post("/create_super_user")
# async def create_super_user(user: CreateSuperUser,database=database_dep):
#    try:
#         create_user = models.User(**user.model_dump())
#         create_user.hashed_password = password.pwd_context.hash(user.hashed_password)
#         database.add(create_user)
#         database.commit()
#         database.refresh(create_user)
#         return {"data":create_user}
#    except Exception as e:
#        return {"error":e}

@router.post("/image/upload")
async def create_post(image: UploadFile = File(...)):
    image_name = image.filename
    image_data = await image.read()
    image_url = upload_image_to_tmp(image_data, image_name)
    return  image_url

@router.post("/post/", response_model=PostRead)
def create_post(post: PostCreate,db = database_dep, current_user = super_user):
    return BlogView(db).create_post(post)

@router.get("/posts/{post_id}", response_model=PostRead)
def get_post(post_id: int,request: Request,response : Response, db = database_dep):
    blog_view = BlogView(db).get_post(post_id,request, response)
    return blog_view

@router.get("/like/{post_id}", response_model=PostRead)
def get_post(post_id: int,request: Request,response : Response, db = database_dep):
    blog_view = BlogView(db).like_post(post_id,request, response, "like")
    return blog_view

@router.get("/dislike/{post_id}", response_model=PostRead)
def get_post(post_id: int,request: Request,response : Response, db = database_dep):
    blog_view = BlogView(db).like_post(post_id,request, response, "dislike")
    return blog_view

@router.get("/posts/", response_model=List[PostRead])
def get_all_posts(db = database_dep):
    return BlogView(db).get_all_posts()

@router.put("/posts/{post_id}", response_model=PostRead)
def update_post(post_id: int, post: PostCreate, db = database_dep, current_user = super_user):
    return BlogView(db).update_post(post_id, post)

@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db = database_dep, current_user = super_user):
    return BlogView(db).delete_post(post_id)


# @router.get("/cookie")
# def func(response : Response, request:Request):
#     response.set_cookie(key = "gfg_cookie_key", value = "gfg_cookie_value")
#     msg = request.cookies.get("gfg_cookie_key")
#     return {"message" :msg}



@router.post("/subscripe")
def subscribe():
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(from_email, to_email, message)
    return {"message":"Success"}