"""
Assessment Task:

URL Shortener API Create a basic URL shortener API using FastAPI and PostgreSQL with these endpoints:

POST /shorten: Accept a long URL, return a shortened URL
GET /{short_code}: Redirect to the original URL Submission:

Implement the API Create a document (Word, Markdown, or TXT) explaining the project and how to run it Upload all files to Google Drive or Dropbox Share a viewable link in your application Time: 1-2 hours We value clean, well-documented code. Focus on demonstrating your FastAPI, PostgreSQL, and API design skills.

Application Process: Complete the assessment task Provide the share link to your project in the application form We look forward to reviewing your work!
"""

from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse, JSONResponse

from sqlalchemy.orm import Session

from .lib import schemas, crud, models, utils
from .lib.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/shorten", response_model=schemas.ShortUrl)
def shorten_url(payload: schemas.ShortenUrlInput, db: Session = Depends(get_db)):
    url = payload.long_url.lower()

    # check is url is valid
    if not utils.is_valid_url(url):
        return JSONResponse(status_code=400, content={"message": "Invalid URL"})

    short_url = crud.create_short_url(db, url)
    return short_url


@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    url = crud.get_url_by_short_code(db, short_code)
    if url:
        return RedirectResponse(str(url.long_url), status_code=301)
    return JSONResponse(status_code=404, content={"message": "URL not found"})
