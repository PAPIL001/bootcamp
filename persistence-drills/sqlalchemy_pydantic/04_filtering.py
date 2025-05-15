from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from pydantic import BaseModel

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

# Function to fetch user by email
def get_user_by_email(email: str) -> UserSchema:
    user = session.query(User).filter(User.email == email).first()
    if user:
        return UserSchema.model_validate(user)
    else:
        return f"User with email {email} not found."

# Test the function with an email
email_to_search = "papil@gmail.com"
user = get_user_by_email(email_to_search)
if isinstance(user, UserSchema):
    print(f"Found user: ID: {user.id}, Name: {user.name}, Email: {user.email}")
else:
    print(user)
