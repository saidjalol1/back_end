from datetime import timedelta
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth import auth_main, token
from pydantics import user_models
from dependencies.dependencies import database_dep
import routes
import routes.category_routes
import routes.post_routest
import routes.tag_routes

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
app.include_router(routes.post_routest.router)
app.include_router(routes.category_routes.router)
app.include_router(routes.tag_routes.router)


@app.get("/")
async def welcome():
    return {"message":"Welcome to Media Blog API"}


@app.post("/token")
async def login(user_token : OAuth2PasswordRequestForm = Depends() ,database = database_dep):
    try:
        user = auth_main.authenticate_user(user_token.username,user_token.hashed_password, database)
        print(user)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "Could not validated the User")
        created_token = token.create_access_token(user.username, user.id, timedelta(minutes=1000))
        return {"access_token": created_token, "token_type": "bearer",}
    except Exception as e:
        print(e)
        return {"error":str(e)}
    