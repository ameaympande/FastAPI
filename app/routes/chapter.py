from typing import List
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from app.database import connect_db

class Chapter(BaseModel):
    title: str
    contents: str

router = APIRouter()

client = connect_db()
db = client["kimo_db"]
collection = db["courses"]


@router.get("/courses/{course_id}/chapters")
async def get_chapters(course_id: str):
    course = collection.find_one({"_id": course_id})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course.get("chapters", [])

@router.get("/courses/{course_id}/chapters/{chapter_title}")
async def get_chapter(course_id: str, chapter_title: str):
    course = collection.find_one({"_id": course_id})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    for chapter in course.get("chapters", []):
        if chapter["title"] == chapter_title:
            return chapter
    raise HTTPException(status_code=404, detail="Chapter not found")

@router.post("/courses/{course_id}/chapters")
async def add_chapter(course_id: str, chapter: Chapter):
    result = collection.update_one(
        {"_id": course_id},
        {"$push": {"chapters": chapter.dict()}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"detail": "Chapter added successfully"}
