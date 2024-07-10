from typing import Optional
from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import user
from db.database import engine
from db import models

app = FastAPI()

# Include routers
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
    return {'message': 'Hello world!'}

# Create the database tables
models.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
