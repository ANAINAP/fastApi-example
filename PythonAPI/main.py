import sys
sys.path.append('/home/oem/Desktop/AXOMIUM/FastApiPython')


from fastapi import FastAPI
from passlib.context import CryptContext
from PythonAPI.router import post,user,auth,votes
from fastapi.middleware.cors import CORSMiddleware

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
# models.Base.metadata.create_all(bind=engine)
app=FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)
# while True:
#     try:
#         conn=psycopg2.connect(host='localhost',database="fastapi",user="postgres",password="anaina@123",cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("database connection was successfull")
#         break
#     except Exception as error:
#         print("connecting to database failed")
#         print("Error:",error)    
#         time.sleep(2)

# my_poss=[{"title":"title of post1","content":"content of post 1","id":1},{"title":"title of post2","content":"content of post 2","id":3}]    
# def find_post(id):
#     for p in my_poss:
#         if p["id"]==id:
#             return p

# def find_index_post(id):
#     for i ,p in enumerate(my_poss):
#         print("enter.................")
#         if p['id']==id :
#             return i           
@app.get("/")
async def root():
    return {"message": "Hello World!!!"}

# @app.get("/get")
# async def root():
#     return {"message": "Nothing"}   

# @app.post("/post") 
# async def msg():
#     posts=cursor.execute("""SELECT * FROM posts""")
#     post=cursor.fetchall()
#     print(post)
#     return {"data":my_poss}

# @app.post('/createpost',status_code=status.HTTP_201_CREATED)
# def addpost(req:post):
#     cursor.execute("""INSERT INTO posts (title,content,published) values(%s,%s,%s) RETURNING *""",(req.title,req.content,req.published))
#     p=cursor.fetchone()
#     print(p)
#     conn.commit()
#     return{"messages":"Post created successfully"
#            }         
# @app.get("/posts/{id}")
# def get_post(id:int,response:Response):
#     print(id)
#     cursor.execute(""" SELECT * FROM posts WHERE id= %s""",(str(id)))
#     f=cursor.fetchone()
#     return {"success"}


# @app.delete("/delt/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int):
#     cursor.execute("""DELETE FROM posts where id =%s returning *""",(str(id)))
#     dl=cursor.fetchone()
#     conn.commit()
#     print(dl)
#     if dl==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"message" :"not found"})
#     return Response(status_code=status.HTTP_204_NO_CONTENT)  
# @app.put("/updating/{id}")
# def update_post(id:int,post:post):

#     cursor.execute("""UPDATE POSTS SET title= %s,content=%s,published=%s where id=%s returning *""",(post.title,post.content,post.published,str(id)))
#     up=cursor.fetchone()
#     conn.commit()
#     print(up)
#     return {"message":"updated"}    
# @app.put("/updating/{id}")
# def update_post(id:int,post:post):

#     index=find_index_post(id)

#     post_dict=post.dict()
#     post_dict['id']=id
#     my_poss[index]=post_dict
#     return {"message":"updated"}    
# @app.delete("/delt/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int):
#     index=find_index_post(id)
#     my_poss.pop(index)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)  

# @app.get("/posts/{id}")
# def get_post(id:int,response:Response):
#     print(id)
#     post=find_post(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"message" :"not found"})
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return {"message" :"not found"}

#     return {"post_detail":post}

# @app.post('/createpost',status_code=status.HTTP_201_CREATED)
# def addpost(req:post):
#     print(req.title)
#     data=req.dict()
#     data['id']=randrange(1,1000)
#     my_poss.append(data)
#     print(my_poss)
#     return{"messages":"Post created successfully",
#            "data":data
#            }      

# @app.post("/post2") 
# async def msg2(payload:dict=Body(...)):
#     print(payload)
#     return {"new_post":f"title : {payload['title']} content:{payload['content']}"}
# @app.post("/post3") 
# async def msg2(post:post):
#     print(post.title)
#     print(post.content)
#     return {"data":"new post"}
# @app.post("/post4") 
# async def msg():
#     return {"message":my_poss}

  

# @app.get("/posts/latest")
# def get_latest():
#     post=my_poss[len(my_poss)-1]
#     return {"details":post}  




