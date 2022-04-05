from operator import index
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database.conection import Base

class UserTable(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    email = Column(String, unique=True, index = True)
    password = Column(String, index = True)
    google = Column(Boolean, index = True)
    is_activate = Column(Boolean, index = True)
    phone = Column(Integer, index = True)

    ventas =  relationship("VentasTable", back_populates = "owner")

class VentasTable(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key = True, index = True)
    tour_name = Column(String, index=True)
    cost = Column(Integer, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))

    owner = relationship("UserTable", back_populates = "ventas")
    clientid = relationship("ClienteTable", back_populates = "client")

class ClienteTable(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    email = Column(String, index = True)
    phone = Column(Integer, index = True)

    client = relationship("VentasTable", back_populates = "clientid")


    