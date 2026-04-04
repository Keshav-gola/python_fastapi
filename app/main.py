from fastapi import FastAPI
from . import models
from .database import engine
from .router import posts, auth, user, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["https://www.google.com", "https://www.youtube.com", "http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],    
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(posts.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}