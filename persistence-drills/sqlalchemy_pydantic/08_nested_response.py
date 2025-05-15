from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, joinedload
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
        from_attributes = True


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    posts: List[PostSchema]  # This will hold a list of posts

    class Config:
        from_attributes = True


# Setup the database engine and session
DATABASE_URL = "sqlite:///users_and_posts.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)


# Fetch user along with their posts (using eager loading)
def fetch_user_and_posts(user_id: int):
    session = SessionLocal()

    # Query the user and their posts using eager loading
    user = session.query(User).options(joinedload(User.posts)).filter(User.id == user_id).first()

    # Close the session
    session.close()

    if user:
        # Convert the result into a Pydantic model using model_validate instead of from_orm
        user_data = UserSchema.model_validate(user)  # Using model_validate()
        return user_data
    else:
        return {"message": "User not found"}


# Example usage: Fetching user with ID 1 and their posts
if __name__ == "__main__":
    user_data = fetch_user_and_posts(1)
    print(user_data.model_dump_json(indent=4))