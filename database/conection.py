from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Ed.2428pe@localhost/postgres"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Ed.2428pe@localhost/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# con = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

