from fastapi import FastAPI
from app.database import connect_db
from app.routes import course, chapter

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    connect_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to the KIMO API"}

app.include_router(course.router, prefix="/courses", tags=["Courses"])
app.include_router(chapter.router, prefix="/chapters", tags=["Chapters"])
