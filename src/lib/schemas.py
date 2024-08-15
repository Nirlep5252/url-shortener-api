from pydantic import BaseModel


class ShortenUrlInput(BaseModel):
    long_url: str


class ShortUrl(BaseModel):
    short_url: str
    long_url: str
