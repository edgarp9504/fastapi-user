from sqlalchemy.orm import Session
from fastapi import HTTPException

# library own 
from middleware.security import get_password, verify_password
from middleware.secutiryjwt import create_jwt, verify_jwt
from models.usersmodel import UserTable,VentasTable
import schemal.user as schemal 




def login(db : Session, email : str, password : str):
    
    try:
            
        search_user = db.query(UserTable).filter(UserTable.email == email).first()
        
        if search_user is None:
            raise HTTPException(status_code= 404, detail= 'no exist email')
        ps = verify_password(password , search_user.password)
        
        if ps is False:
            raise HTTPException(status_code= 404, detail= 'invalid password')

        user_login =schemal.User( email= search_user.email, is_activate= search_user.is_activate, name=search_user.name,id = search_user.id, google= search_user.google)
        
        # Create JWT
        token = create_jwt({"user" : search_user.name})
    
    except:
        raise HTTPException(status_code= 404, detail= 'no se pudo logear')
    


    return { 'email' : user_login.email, 'token' :{ 'access_token' : token, 'token_type' : "bearer"}}

async def verify_token( db : Session ,token : str):
    
    try:
        jwt_decode = verify_jwt(token)
        print(jwt_decode)
    except:
        raise HTTPException(status_code= 404, detail= 'token caucado')
    
    return 'jwt'



def get_user(db: Session,  user_id : int):
    user = db.query(UserTable).filter(UserTable.id == user_id).first()
    new_user = schemal.User(**user)
    return new_user

def get_user_by_email(db : Session, email: str):
    return db.query(UserTable).filter(UserTable.email == email).first() 

def get_users(db: Session, skip : int = 0, limit : int = 100):
    query = db.query(UserTable.id ,UserTable.name, UserTable.email, UserTable.google, UserTable.is_activate)
    user = query.filter( UserTable.is_activate == True).offset(skip).limit(limit).all()
    return user

def create_user(db : Session, user : schemal.User):
    validate_email = get_user_by_email(db, user.email)
    if validate_email:
        raise HTTPException(status_code= 404, detail= 'email already register')
    db_user = UserTable( 
                
                google = True, 
                password = get_password(user.password), 
                email = user.email,
                is_activate = True
                )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user

def baja_user(db : Session,  id = int):
    confirm_user = db.query(UserTable).filter(UserTable.id == id).first()
    if confirm_user is None :
        raise HTTPException(status_code= 404, detail= 'not exist user') 
    db.query(UserTable).filter(UserTable.id == id).update({'is_activate' : False})
    db.commit()
    return 'Usuario Actualizado'

def update_user(db : Session, user : schemal.User, id : int ):
    confirm_user = get_user(db,user_id=id)
    if confirm_user is None :
        raise HTTPException(status_code= 404, detail= 'not exist user') 
    db.query(UserTable).filter(UserTable.id == id).update({'name': user.name, 'email' : user.email, 'password': user.password})
    db.commit()
    return user


def get_ventas(db : Session, skip : int = 0, limit : int = 100):
    return db.query(VentasTable).offset(skip).limit(limit).all()

def create_ventas(db : Session, dbVentas : schemal.Ventas, user_id : int, clientid : int):
    db_ventas = VentasTable(tour_name = dbVentas.tour_name , cost = dbVentas.cost , owner_id = user_id, client_id = clientid)
    db.add(db_ventas)
    db.commit()
    db.refresh(db_ventas)
    return db_ventas


