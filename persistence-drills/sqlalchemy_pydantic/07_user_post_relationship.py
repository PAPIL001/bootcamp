from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from pydantic import BaseModel

# SQLAlchemy setup
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    # Relationship to Post
    posts = relationship("Post", back_populates="author")


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationship to User
    author = relationship("User", back_populates="posts")


# Pydantic models
class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    posts: list

    class Config:
        from_attributes = True


class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    class Config:
        from_attributes = True


# Database setup
engine = create_engine("sqlite:///users_and_posts.db")
Session = sessionmaker(bind=engine)
session = Session()

# Create tables in the database
Base.metadata.create_all(engine)


# Function to create a new user with posts
def create_user_with_posts(name: str, email: str, posts_data: list):
    user = User(name=name, email=email)
    for post_data in posts_data:
        post = Post(**post_data)
        user.posts.append(post)
    session.add(user)
    session.commit()
    print(f"User {name} with posts created successfully.")


# Example usage
posts = [
    {"title": "First Post", "content": "This is my first post."},
    {"title": "Second Post", "content": "This is my second post."}
]
create_user_with_posts("xyz", "xyz@gmail.com", posts)
