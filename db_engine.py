import logging
from typing import AsyncIterator
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.exc import SQLAlchemyError
from settings import db_settings
from sqlalchemy.ext.declarative import declarative_base

logger = logging.getLogger(__name__)

async_engine = create_async_engine(
    db_settings.DB_URL.format(
        db_settings.POSTGRES_USER,
        db_settings.POSTGRES_PASSWORD,
        db_settings.POSTGRES_HOST,
        db_settings.POSTGRES_PORT,
        db_settings.POSTGRES_DB,
    ),
    echo=True  # output all queries goes to database
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)


async def get_session() -> AsyncIterator[async_sessionmaker]:  # for DI
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except SQLAlchemyError as e:
            logger.exception(e)


Base = declarative_base()
