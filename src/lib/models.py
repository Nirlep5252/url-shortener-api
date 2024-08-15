from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base


class ShortUrl(Base):
    __tablename__ = "short_urls"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    short_url = Column(String, index=True)
    long_url = Column(String, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now())
    updated_at = Column(DateTime, default=lambda: datetime.now())
