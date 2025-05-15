from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

engine = create_engine("sqlite:///users.db")
Base.metadata.create_all(engine)

print("Database and model created.")
