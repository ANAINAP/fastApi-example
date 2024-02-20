from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import  Optional
from pydantic.types import conint

class userCreate(BaseModel):
    email:EmailStr
    password:str    


class userOut(userCreate):
    id:int
    created_at:datetime    
    class Config:
        orm_mode=True


class postBase(BaseModel):
    title:str
    content:str
    published:bool=True

class postCreate(postBase):
    pass

class post(BaseModel):
    id:int
    title:str
    content:str
    published:bool=True
    created_at:datetime
    owner:userOut

    class Config:
        orm_mode=True
    
class postOut(BaseModel):    
    Post:post
    votes:int

    class Config:
        orm_mode=True
    

class userLogin(BaseModel):
    email:EmailStr
    password:str    

class Token(BaseModel):
    access_token:str
    token_type:str


class TokenData(BaseModel):
    id: Optional[str] =None


class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)
