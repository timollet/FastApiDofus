from conf import config
import psycopg2


def connect():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(params)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return conn
