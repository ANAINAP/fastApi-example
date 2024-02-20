from .. import models,schema,oauth2
from ..database import get_db
from fastapi import status
from fastapi import Response,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List,Optional

router=APIRouter()


@router.get('/sqlalchemy')
def testpost(db: Session = Depends(get_db)):
    post=db.query(models.Post).all()
    return {"data":post}

@router.post('/createpost',status_code=status.HTTP_201_CREATED)
def addpost(req:schema.postCreate,db: Session = Depends(get_db),response_model=schema.post ,current_user:int=Depends((oauth2.get_current_user))):

    print(current_user.id)
    # print(current_user.email)
    new_post=models.Post(owner_id=current_user.id,**req.dict())
    print(new_post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    print(current_user.email)
    return new_post
           
@router.get("/getposts",response_model=List[schema.postOut])
def get_post(db: Session = Depends(get_db),response_model=schema.post ,current_user:int=Depends((oauth2.get_current_user)),limit:int=10,skip:int=0,search:Optional[str]=""):
    post=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).all()
    # post=db.query(models.Post).filter(models.Post.owner_id==current_user.id).all()
    print(post)
    result=db.query(models.Post,func.count(models.Votes.post_id).label("votes")).join(models.Votes,models.Votes.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).all()
    print(f"result {result}")
    # if not post:
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"message" :"not found"})
    return result

@router.get("/getposts/{id}",response_model=schema.postOut)
def get_post(id:int,db: Session = Depends(get_db),response_model=schema.post ,current_user:int=Depends((oauth2.get_current_user))):
    # print(id)
    # post=db.query(models.Post).filter(models.Post.id==id).first()
    # print(post)

    result=db.query(models.Post,func.count(models.Votes.post_id).label("votes")).join(models.Votes,models.Votes.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"message" :"not found"})
    return result
#
@router.delete("/delt/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db),current_user:int=Depends((oauth2.get_current_user))):
    post_query=db.query(models.Post,func.count(models.Votes.post_id).label("votes")).filter(models.Post.id==id)
    post=post_query.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"message" :"not found"})
    print(f"user {oauth2.get_current_user}")
    if post.owner_id!=oauth2.get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not autherized to perform requested action")
    post_query.delete(synchronize_session=False)
    db.commit()
   
    
    return Response(status_code=status.HTTP_204_NO_CONTENT) 

@router.put("/updating/{id}")
def update_post(id:int,req:schema.postCreate,db: Session = Depends(get_db),current_user:int=Depends((oauth2.get_current_user))):
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"message" :"not found"})
    if post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not autherized to perform requested action")
    post_query.update(req.dict(),synchronize_session=False)
    db.commit()
    return {"message":"updated"} 
