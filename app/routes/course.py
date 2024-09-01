from fastapi import APIRouter, HTTPException, Query
from app.database import connect_db
from bson import ObjectId

router = APIRouter()
client = connect_db()
db = client["kimo_db"]

@router.get("/")
def get_courses(sort_by: str = "name", domain: str = None):
    sort_field = {
        "name": "name",
        "date": "date",
        "rating": "rating"
    }.get(sort_by, "name")

    query = {}
    if domain:
        query['domain'] = domain

    try:
        courses = list(db.courses.find(query).sort(sort_field, -1))
        return {"courses": courses}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{course_id}")
def get_course(course_id: str):
    try:
        course_id = ObjectId(course_id)
        course = db.courses.find_one({"_id": course_id})
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        return course
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
