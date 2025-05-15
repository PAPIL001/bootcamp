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

# Function to delete a user
def delete_user(user_id: int) -> str:
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return f"User ID {user_id} has been deleted."
    else:
        return f"User ID {user_id} not found."

# Test the function to delete a user
user_id_to_delete = 1
result = delete_user(user_id_to_delete)
print(result)
