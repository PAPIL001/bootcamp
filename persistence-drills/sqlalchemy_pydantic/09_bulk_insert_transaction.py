from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from typing import List

# Define SQLAlchemy Base
Base = declarative_base()


# Define User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    # Relationship with Post
    posts = relationship("Post", back_populates="author")


# Define Post model
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationship with User
    author = relationship("User", back_populates="posts")


# Pydantic models to structure the data
class PostSchema(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True  # Updated for Pydantic V2


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    posts: List[PostSchema]  # This will hold a list of posts

    class Config:
        from_attributes = True  # Updated for Pydantic V2


# Setup the database engine and session
DATABASE_URL = "sqlite:///users_and_posts.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


# Insert multiple users within a transaction
def insert_multiple_users(user_data_list: List[dict]):
    session = SessionLocal()

    try:
        for user_data in user_data_list:
            # Check if email already exists in the database
            existing_user = session.query(User).filter(User.email == user_data['email']).first()

            if existing_user:
                print(f"User with email {user_data['email']} already exists. Skipping insert.")
                continue  # Skip inserting this user

            user = User(**user_data)
            session.add(user)

        # Commit transaction to the database
        session.commit()
        print(f"Successfully inserted {len(user_data_list)} users.")

    except Exception as e:
        # Rollback the transaction in case of error
        session.rollback()
        print(f"Error occurred while inserting users: {e}")

    finally:
        # Close session
        session.close()


# Example usage: Inserting multiple users
if __name__ == "__main__":
    users_to_insert = [
        {"name": "xyz", "email": "xyz@gmail.com"},
        {"name": "abc", "email": "abc@gmail.com"},
        
    ]

    insert_multiple_users(users_to_insert)
