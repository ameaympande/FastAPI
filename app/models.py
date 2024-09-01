from pydantic import BaseModel
from typing import List

class Chapter(BaseModel):
    title: str
    contents: str
    rating: int = 0

class Course(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]
    rating: int = 0
