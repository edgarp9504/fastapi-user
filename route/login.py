from fastapi import APIRouter, Depends, Header
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session

# library ow
import crud.cruduser  as controller
import database.conection as conn

app_login = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


# Dependency
def get_db():
    db = conn.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app_login.post("/login" )
def login(form_data: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db) ):
    return controller.login(db, email= form_data.username, password = form_data.password)

@app_login.get("/items/")
async def read_items(token: str = Header(None)):
    return {"X-Token values": token}
