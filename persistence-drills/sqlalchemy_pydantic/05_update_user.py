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

# Function to update user email
def update_user_email(user_id: int, new_email: str) -> str:
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.email = new_email
        session.commit()
        return f"User ID {user_id}'s email updated to {new_email}."
    else:
        return f"User ID {user_id} not found."

# Test the function to update an email
user_id_to_update = 1
new_email = "xyz@gamil.com"
result = update_user_email(user_id_to_update, new_email)
print(result)
