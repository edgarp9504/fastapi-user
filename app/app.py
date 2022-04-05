from fastapi import FastAPI
from route.user import app_user
from route.client import app_client
from route.login import app_login


app = FastAPI( title="APIEdgar" )

app.include_router(app_login, tags=["login"])
app.include_router(app_user, prefix= "/api" , tags=["user"])
app.include_router(app_client, prefix= "/api", tags=["client"])
