import logging
logging.getLogger("sqlalchemy.engine").setLevel(logging.ERROR)


import asyncio
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.future import select

# Async SQLAlchemy Base
Base = declarative_base()

# Models
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    posts = relationship("Post", back_populates="author")


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="posts")


# PostgreSQL async engine using asyncpg
DATABASE_URL = "postgresql+asyncpg://postgres:Papil%5676@localhost/test_async_db"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database initialized.")


async def insert_users():
    async with AsyncSessionLocal() as session:
        async with session.begin():  # begins a transaction
            users = [
                User(name="xyz", email="xyz@gmail.com"),
                User(name="abc", email="abc@gmail.com"),
            ]
            session.add_all(users)
        print("✅ Users inserted.")


async def fetch_users():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")


async def main():
    await init_db()
    await insert_users()
    await fetch_users()


if __name__ == "__main__":
    asyncio.run(main())
