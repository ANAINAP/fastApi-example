from .. import models,utils,schema
from ..database import SessionLocal,get_db
from fastapi import status
from fastapi import HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session

router=APIRouter()

@router.post("/createuser/",status_code=status.HTTP_201_CREATED,response_model=schema.userOut)
def create_user(user:schema.userCreate,db: SessionLocal = Depends(get_db)): # type: ignore
    hashed_password=utils.hash(user.password)
    user.password=hashed_password
    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/user/{id}",response_model=schema.userOut)
def getuser(id:int ,db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail=f"user with id :{id} not found")
    return user