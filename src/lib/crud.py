import hashlib
from sqlalchemy.orm import Session

from . import models


def get_url_by_short_code(db: Session, short_code: str) -> models.ShortUrl | None:
    return (
        db.query(models.ShortUrl)
        .filter(models.ShortUrl.short_url == short_code)
        .first()
    )


def create_short_url(db: Session, long_url: str) -> models.ShortUrl:
    # check if already exists
    db_short_url = (
        db.query(models.ShortUrl).filter(models.ShortUrl.long_url == long_url).first()
    )
    if db_short_url:
        return db_short_url

    # create new short url
    short_url = hashlib.md5(long_url.encode()).hexdigest()[:6]
    db_short_url = models.ShortUrl(short_url=short_url, long_url=long_url)
    db.add(db_short_url)
    db.commit()
    db.refresh(db_short_url)
    return db_short_url
