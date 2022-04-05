from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


# own library
from schemal.client import Client
import database.conection as conn
import models.usersmodel as models
import crud.crudclient as crud

models.Base.metadata.create_all(bind=conn.engine)
conn.engine.connect()
app_client = APIRouter()


def get_db():
    db = conn.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app_client.post("/clients", response_model= Client)
def create_user( client : Client, db: Session = Depends(get_db) ):
    return crud.create_client(db,client=client)