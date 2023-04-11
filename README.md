# FastApiDofus

## install module
pip3 install SQLAlchemy
pip3 install databases
pip3 install DateTime
pip3 install typing
pip3 install uuid
pip3 install pydantic
pip3 install passlib

## DB Script
create user usertest with NOINHERIT LOGIN ENCRYPTED PASSWORD 'usertest222';
create database dbtest owner=usertest;

## How to run
```uvicorn main:app --reload```