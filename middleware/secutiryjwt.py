from base64 import encode
from fastapi import HTTPException
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date

def create_jwt(data):
    signed = jwt.encode({**data, 'exp': expire_date(2)}, SECRET_KEY , algorithm=ALGORITHM)
    return signed

def verify_jwt(token = str):
    try:
        to_decode = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    
    except:
        raise HTTPException(status_code= 404, detail= 'token caucado')
    
    return to_decode 