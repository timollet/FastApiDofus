from fastapi import FastAPI, status
import psycopg2
import db_utils
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    user_id: int
    username: str


@app.get("/")
async def root():
    return {"message": "Home page"}


@app.get("/users")
async def get_users():
    query = ("select user_id,"
             "username "
             "from users_table")
    conn = db_utils.connect()
    cur = conn.cursor()
    cur.execute(query)
    raw = cur.fetchall()
    # Close connection
    conn.close()
    return raw


@app.get("/users/{id}")
async def get_user_by_id(id):
    query = (f"select user_id,"
             f"username "
             f"from users_table "
             f"Where user_id = {id}")
    # Open connection
    conn = db_utils.connect()
    # Open a cursor to send SQL commands
    cur = conn.cursor()
    cur.execute(query)
    raw = cur.fetchall()
    # Close connection
    conn.close()
    return raw


@app.get("/users/{user_id}/name")
async def get_username_by_id(user_id):
    query = (f"select username "
             f"from users_table "
             f"Where user_id = {user_id}")
    # Open connection
    conn = db_utils.connect()
    # Open a cursor to send SQL commands
    cur = conn.cursor()
    cur.execute(query)
    raw = cur.fetchall()
    # Close connection
    conn.close()
    return raw


@app.post("/users/{user_id}/{name}", status_code=status.HTTP_201_CREATED)
async def create_user(user_id, name):
    query2 = ("INSERT INTO users_table (user_id, username) VALUES (%d,%s)",(user_id, name))
    # Open connection
    conn = db_utils.connect()
    # Open a cursor to send SQL commands
    cur = conn.cursor()
    cur.execute(query2)
    cur.close()
    conn.commit()
    # raw = cur.fetchall()
    # Close connection
    conn.close()
    return {"1"}
