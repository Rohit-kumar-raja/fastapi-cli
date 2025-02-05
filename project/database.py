from fastapi.concurrency import asynccontextmanager
from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from .settings import settings


class Database:
    # PostgreSQL connection string for asyncpg
    DATABASE_URL: str = (
        f"postgresql+asyncpg://{settings.db_username}:{settings.db_password}"
        f"@{settings.db_host}:{settings.db_port1}/{settings.db_database}"
    )

    def __init__(self):
        # Create an async engine
        self.engine = create_async_engine(self.DATABASE_URL, echo=True)

        # Async session factory
        self.AsyncSessionLocal = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=True,
            autoflush=False,
        )

    @asynccontextmanager
    async def get_db(self):
        """Provide a new async session for database operations."""
        async with self.AsyncSessionLocal() as session:
            try:
                yield session
            finally:
                await session.close()
