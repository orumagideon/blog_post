from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix="/blogs",
    tags=["blogs"]
)

class Image(BaseModel):
    url:str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool] = None
    tags: List[str] = []
    metadata: Dict[str,str] = {"key1": "value1"}
    image: Optional[Image] = None

@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        "id": id,
        "data": blog,
        "version": version
    }

@router.post("/new/{id}/comment/{comment_id}")
def create_comment(
    id: int,
    comment_id: int = Path(..., gt=5, le=10),
    blog: BlogModel = Body(...),
    comment_title: Optional[int] = Query(
        None,
        title="Title of the comment",
        description="Some description of comment_title",
        alias="commentTitle",
        deprecated=True
    ),
    content: str = Body(
        ...,
        min_length=10,
        max_length=50,
        regex=r"^[a-z\s]*$"
    ),
    v: Optional[List[str]] = Query(["1.0", "1.1", "1.2"])
):
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "version": v,
        "comment_id": comment_id
    }