from fastapi import HTTPException
from sqlalchemy.orm import Session 


from models.usersmodel import ClienteTable
from schemal.client import Client

def get_email(db : Session, email : str):
    return db.query(ClienteTable).filter(ClienteTable.email == email).first()

def create_client(db: Session, client = Client ):
    validate_email = get_email(db, client.email)
    if validate_email:
        raise HTTPException(status_code = 404, detail = 'email already register')

    db_client = ClienteTable(
                name = client.name, 
                email = client.email, 
                phone = client.phone
                )

    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    
    return db_client