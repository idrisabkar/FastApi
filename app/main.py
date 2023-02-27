from fastapi import FastAPI
from .database import  engine
import sys
sys.path.append('D:\\UI\\Python\\FastApi\\app')
from . import models
from routers import posts,users,authentication,likes
from fastapi.middleware.cors import CORSMiddleware
#db: Session = Depends(get_db)

models.Base.metadata.create_all(bind=engine)


# while True:
#    try:
#        with psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='user_idris2014',
#                              cursor_factory=RealDictCursor) as con:
#            print("Successfully connected to database")
#            cursor = con.cursor()
#            break
#    except Exception as error:
#        print(error)
#

#def getUserBy_user_id(user_id: int):
#    # cursor.execute(""" SELECT * from users where user_id = (%s)""", (user_id,))
#    # user = cursor.fetchone()
#    session_ = sessionmaker(bind=engine)
#    session = session_()
#    user = session.query(models.Users).filter(models.Users.user_id == user_id).first()
#    return user


# def del_user(user_id):
#    cursor.execute(""" DELETE from users where user_id = %s""", (user_id,))
#    con.commit()


app = FastAPI()


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(authentication.router)
app.include_router(likes.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"Message": "Hello world"}




