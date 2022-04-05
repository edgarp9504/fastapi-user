from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

# library ow
from schemal.user import User, UserBase, VentasBase
import crud.cruduser  as controller
import database.conection as conn
from route.login import oauth2_scheme

app_user = APIRouter()


# Dependency
def get_db():
    db = conn.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app_user.get("/users")
async def getuser_list( db : Session = Depends(get_db) , skip : int = 0, limit : int = 100,  token : str = Depends(oauth2_scheme)):
    users = controller.get_users( db, skip=skip, limit=limit)
    return users


@app_user.post('/users', response_model= UserBase)
def create_user(user: UserBase, db : Session = Depends(get_db),  token : str = Depends(oauth2_scheme)):
    return controller.create_user(db, user=user)

@app_user.post('/users/ventas')
def create_venta(dbVenta: VentasBase, user_id : int, client_id : int , db : Session = Depends(get_db), token : str = Depends(oauth2_scheme) ): 
    print(client_id)
    return controller.create_ventas(db,dbVenta, user_id,client_id)

@app_user.put('/users/{id_user}')
def update_user( user : UserBase ,id_user:int , db : Session = Depends(get_db),  token : str = Depends(oauth2_scheme)):
    return controller.update_user(db, user, id=id_user)

@app_user.delete('/users/{id_user}')
def delete_user( id_user:int , db : Session = Depends(get_db),  token : str = Depends(oauth2_scheme)):
    return controller.baja_user(db, id=id_user)


