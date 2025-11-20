from pydantic import BaseModel
from typing import Optional
from pydantic_config_generator import prompt, write_ini, write_env


class ExampleSubConfig(BaseModel):
    name: str = None
    surname: str
    age: int


class ExampleConfig(BaseModel):
    name: str = ''
    surname: str
    alias: Optional[str]
    height: int = None
    age: int
    is_student: bool = True
    favorite_teacher: ExampleSubConfig = None

class ExampleSuperConfig(BaseModel):
    student: ExampleConfig
    teacher: ExampleSubConfig


config = prompt(ExampleSubConfig)
print(config)

write_ini(config)
write_env(config)
