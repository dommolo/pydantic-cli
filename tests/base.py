from pydantic import BaseModel
from typing import Optional
from pydantic_config_generator import prompt, write_ini, write_env


class Teacher(BaseModel):
    students: int = 0
    name: str = None
    surname: str
    age: int


class Student(BaseModel):
    name: str = ''
    surname: str
    alias: Optional[str]
    height: int = None
    age: int
    is_student: bool = True
    teacher: Teacher = None

class Thesis(BaseModel):
    student: Student
    teacher: Teacher


config = prompt(Teacher)
print(config)

write_ini(config)
write_env(config)
