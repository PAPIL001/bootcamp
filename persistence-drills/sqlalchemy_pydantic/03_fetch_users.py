from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from pydantic import BaseModel
from typing import List

# SQLAlchemy setup
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Pydantic model
class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

# Database setup
engine = create_engine("sqlite:///users.db")
Session = sessionmaker(bind=engine)
session = Session()

# Fetch users from database
users = session.query(User).all()

# Convert to list of Pydantic models
user_schemas: List[UserSchema] = [UserSchema.model_validate(user) for user in users]

# Print in structured format
for user in user_schemas:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
