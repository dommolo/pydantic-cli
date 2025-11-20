import configparser
from pathlib import Path
from pydantic import BaseModel
import sys
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


def prompt_config(config: BaseModel, group: str = None) -> BaseModel:
    output = {}

    if group is None:
        group = config.__name__ + '.'

    for k, v in config.__fields__.items():
        if issubclass(v.type_, BaseModel):
            if not v.required:
                s = input(f'{group}{v.name} is optional. Skip? (y/n) [n]: ')
                if s == 'y':
                    continue

            output[k] = prompt_config(v.type_, group=f'{group}{v.name}.')
        else:
            output[k] = prompt_value(v, output.get(k, v.default), group)

    return output


def prompt(config_class: BaseModel):
    while True:
        try:
            data = prompt_config(config_class)
            return config_class(**data)
        except Exception as e:
            print(f"Error: {e}")
            continue


def check_file(file: str):
    if Path(file).is_file():
        confirm = input(f'File {file} already exists, overwrite? (y/n): ')
    else:
        confirm = 'y'

    if confirm != 'y':
        print('Operation cancelled.')
        sys.exit(1)


def write_ini(data: BaseModel, file: str = 'config.ini'):
    def add_section(config: configparser.ConfigParser, name: str, subdata: dict):
        config.add_section(name)
        for key, value in subdata.items():
            if isinstance(value, dict):
                add_section(config, key, value)
            else:
                config.set(name, key, str(value))

    config = configparser.ConfigParser()
    add_section(config, 'default', data.dict())

    with open(file, 'w') as f:
        config.write(f)

    print(f'File {file} created successfully.')


def write_env(data: BaseModel, file: str = '.env', group_separator: str = '.', use_uppercase: bool = True):
    def add_group(group: str, subdata: dict):
        output = ''
        for key, value in subdata.items():
            name = key.upper() if use_uppercase else key

            if isinstance(value, dict):
                output += add_group(f'{name}{group_separator}', value)
            else:
                output += f'{group}{name}={value}\n'

        return output

    output = add_group('', data.dict())
    with open(file, 'w') as f:
        f.write(output)

    print(f'File {file} created successfully.')


def create_ini(config: BaseModel, file: str = 'config.ini'):
    check_file(file)

    data = prompt(config)
    write_ini(data, file)


def create_env(config: BaseModel, file: str = '.env', group_separator: str = '.', use_uppercase: bool = True):
    check_file(file)

    data = prompt(config)
    write_env(data, file, group_separator, use_uppercase)
