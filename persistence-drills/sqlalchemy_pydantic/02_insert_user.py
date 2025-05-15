from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel, EmailStr, ValidationError

# SQLAlchemy setup
Base = declarative_base()
engine = create_engine("sqlite:///users.db")
Session = sessionmaker(bind=engine)

# SQLAlchemy model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Pydantic model
class UserSchema(BaseModel):
    name: str
    email: EmailStr

    class Config:
        from_attributes = True

# Input data
input_data = {"name": "Papil", "email": "papil@gmail.com"}

# Validate with Pydantic
try:
    validated = UserSchema(**input_data)
except ValidationError as e:
    print("Validation error:", e)
    exit(1)

# Insert into DB
session = Session()
user = User(name=validated.name, email=validated.email)
session.add(user)
session.commit()
session.close()

print(f"Inserted user: {validated.name}, {validated.email}")
