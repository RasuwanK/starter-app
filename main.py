from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
	name: str
	description: str | None = None
	image_url: str
	likes: int

@app.post("/posts")
async def get_posts(post: Post):
	return post