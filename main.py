from os import name
from fastapi import FastAPI
from users import models
from db.database import engine
import users.router as user_router
import comments.router as comment_router
import posts.router as posts_router
from auth import authentication
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import  add_pagination
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(user_router.router)
app.include_router(authentication.router)
app.include_router(posts_router.router)
app.include_router(comment_router.router)


@app.get("/")
def root():
    return "Bienvenidos a la api!."


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(engine)

add_pagination(app)

app.mount('/images', StaticFiles(directory='images'), name='images')
