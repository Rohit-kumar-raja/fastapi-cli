from fastapi.concurrency import asynccontextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from .settings import environment_variables as  settings


class Database:
    # PostgreSQL connection string for asyncpg
    DATABASE_URL: str = (
        f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}"
        f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
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


database = Database()
db = database.get_db()

async_engine = create_async_engine(Database.DATABASE_URL, echo=True)
sync_engine = create_engine(Database.DATABASE_URL, echo=True)
