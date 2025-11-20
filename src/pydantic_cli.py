from pydantic import BaseModel
from typing import Any


def prompt_value(item, default: Any, group: str = '') -> Any:
    while True:
        v = input(f"{group}{item.name} [{default}]: ")

        if item.required and v == '':
            print(f"Error: {item.name} is required")
            continue

        out = default if v == '' else v

        vv, verr = item.validate(out, {}, loc=item.name)
        if verr:
            print(f"Error: expected {item.type_} but got {type(out)}")
            continue

        return vv


def prompt_config(config: BaseModel, group: str = '.') -> BaseModel:
    output = {}

    for k, v in config.__fields__.items():
        if issubclass(v.type_, BaseModel):
            if not v.required:
                s = input(f'{v.name} is optional. Skip? (y/n) [n]: ')
                if s == 'y':
                    continue

            output[k] = prompt_config(v.type_, group=f'{group}{v.name}.')
        else:
            output[k] = prompt_value(v, output.get(k, v.default), group)

    return output


def run(config_class: BaseModel):
    while True:
        try:
            data = prompt_config(config_class)
            return config_class(**data)
        except Exception as e:
            print(f"Error: {e}")
            continue
