from fastapi import HTTPException, status, Depends,APIRouter
from app.database import get_db
from sqlalchemy.orm import Session
import sys
sys.path.append('D:\\UI\\Python\\FastApi\\app')
import models
import schemas


router = APIRouter(prefix="/posts",tags=["Posts"])



@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponseModel)
def create_post(post:schemas.CreatePost,db:Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{post_id}",response_model=schemas.PostResponseModel)
def get_post_by_id(post_id : int,db : Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return post

@router.delete("/{post_id}",status_code=status.HTTP_204_NO_CONTENT)
def del_post(post_id : int,db : Session = Depends(get_db)):
   post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
   if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
   db.delete(post)
   db.commit()
   
@router.get("/",response_model=list[schemas.PostResponseModel])
def get_posts(db : Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts