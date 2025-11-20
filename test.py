from pydantic import BaseModel
from pydantic_cli import run

class ExampleSubConfig(BaseModel):
    name: str
    surname: str
    age: int

class ExampleConfig(BaseModel):
    name: str = ''
    surname: str
    age: int
    is_student: bool = True
    teacher: ExampleSubConfig = None

config = run(ExampleConfig)
print(config)