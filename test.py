from pydantic import BaseModel
from pydantic_config_generator import prompt, write_ini, write_env


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


config = prompt(ExampleConfig)
print(config)

write_ini(config)
write_env(config)
