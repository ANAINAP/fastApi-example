from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from .. import database,models,utils,oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router=APIRouter()

@router.post("/login")
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db: Session = Depends(database.get_db)):
    # 
    print("entered...")
    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()
    if not user:
        raise HTTPException (status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentials")
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentials")
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    return {"token":access_token,"token_type":"bearer"}