from fastapi import FastAPI, status
import db_utils
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Home page"}


@app.get("/users")
async def get_users():
    query = ("select id,"
             "name "
             "from users")
    conn = db_utils.connect()
    cur = conn.cursor()
    cur.execute(query)
    raw = cur.fetchall()
    # Close connection
    conn.close()
    return raw


@app.get("/users/{id}")
async def get_user_by_id(id):
    query = (f"select id,"
             f"name "
             f"from users "
             f"Where id = {id}")
    # Open connection
    conn = db_utils.connect()
    # Open a cursor to send SQL commands
    cur = conn.cursor()
    cur.execute(query)
    raw = cur.fetchall()
    # Close connection
    conn.close()
    return raw


@app.get("/users")
async def get_username_by_id(user_id):
    query = (f"select name "
             f"from users "
             f"Where id = {user_id}")
    # Open connection
    conn = db_utils.connect()
    # Open a cursor to send SQL commands
    cur = conn.cursor()
    cur.execute(query)
    raw = cur.fetchall()
    # Close connection
    conn.close()
    return raw


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(name):
    query2 = "INSERT INTO users (name) VALUES (%s)", (name,)
    # Open connection
    conn = db_utils.connect()
    # Open a cursor to send SQL commands
    cur = conn.execute("INSERT INTO users (name) VALUES (%s)",
                       (name,))
    conn.commit()
    # raw = cur.fetchall()
    # Close connection
    conn.close()
    return {"1"}
