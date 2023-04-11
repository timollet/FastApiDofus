from fastapi import FastAPI, status
import psycopg2
import var_env
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
    # Open connection
    conn = psycopg2.connect(
        f"host={var_env.HOST} dbname={var_env.DATABASE} user={var_env.USER} "
        f"password={var_env.PASSWORD} port={var_env.PORT}")
    # Open a cursor to send SQL commands
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
    conn = psycopg2.connect(
        f"host={var_env.HOST} dbname={var_env.DATABASE} user={var_env.USER} "
        f"password={var_env.PASSWORD} port={var_env.PORT}")
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
    conn = psycopg2.connect(
        f"host={var_env.HOST} dbname={var_env.DATABASE} user={var_env.USER} "
        f"password={var_env.PASSWORD} port={var_env.PORT}")
    # Open a cursor to send SQL commands
    cur = conn.cursor()
    cur.execute(query)
    raw = cur.fetchall()
    # Close connection
    conn.close()
    return raw


@app.post("/user/{user_id}/{name}", status_code=status.HTTP_201_CREATED)
async def post_user(user_id, name):
    query2 = f"INSERT INTO users_table (user_id, username) VALUES ('{user_id}','{name}');"
    # Open connection
    conn = psycopg2.connect(
        f"host=%{var_env.HOST} dbname={var_env.DATABASE} user={var_env.USER} "
        f"password={var_env.PASSWORD} port={var_env.PORT}", autocommit=True)
    # Open a cursor to send SQL commands
    cur = conn.cursor()
    cur.execute(query2)
    cur.close()
    conn.commit()
    # raw = cur.fetchall()
    # Close connection
    conn.close()
    return "1"
