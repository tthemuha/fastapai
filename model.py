from pydantic import BaseModel
from typing import List


class School(BaseModel):
    title: str
    room: List[int]
    teacher: List[str]


class Student(BaseModel):
    name: str
    email: str
    room_id: int
    since: List[str]