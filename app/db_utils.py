from var_env import *
import psycopg

QUERY_DATATABLE_CREATION = "CREATE TABLE id serial primary key,name varchar (50) not null;"


def connect():
    conn = None
    try:
        conn = psycopg.connect(host=host, port=port, dbname=database, user=user, password=password)
    except(Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        return conn
