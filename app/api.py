from fastapi import FastAPI, status
import db_utils
from pydantic import BaseModel
from utils.log_management import log_error, log_message

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
    result = cur.fetchall()
    # Close connection
    conn.close()
    return result


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
    result = cur.fetchone()
    # Close connection
    conn.close()
    return result


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(name):
    try:
        # Open connection
        conn = db_utils.connect()
        # Open a cursor to send SQL commands
        cur = conn.execute("INSERT INTO users (name) VALUES (%s)",
                           (name,))
        conn.commit()
        # raw = cur.fetchall()
        # Close connection
        conn.close()
    except Exception as exception:
        log_error("\n".join(exception.args))
        raise


@app.delete("/users/{id}")
async def delete_user(id):
    try:
        # Open connection
        conn = db_utils.connect()
        # Open a cursor to send SQL commands
        cur = conn.execute("DELETE from users Where id = (%s)",
                           (id,))
        conn.commit()
        # raw = cur.fetchall()
        # Close connection
        conn.close()
    except Exception as exception:
        log_error("\n".join(exception.args))
        raise


@app.put("/users", status_code=status.HTTP_200_OK)
async def create_user(name, id):
    try:
        # Open connection
        conn = db_utils.connect()
        # Open a cursor to send SQL commands
        cur = conn.execute("UPDATE users SET name = %s WHERE  id = (%s); ",
                           (name, id,))
        conn.commit()
        # raw = cur.fetchall()
        # Close connection
        conn.close()
    except Exception as exception:
        log_error("\n".join(exception.args))
        raise
