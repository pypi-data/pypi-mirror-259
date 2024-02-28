"""Load environment variables"""

# Built-in imports
from ast import literal_eval as ast_literal_eval
from json import loads as json_reads
from os import environ

# PIP imports
from dotenv import dotenv_values
from toml import loads as toml_reads
from yaml import safe_load as yaml_reads

# Second-party imports
from .errors import EnvironVarUndeclaredError
from .utils import Path, PathLike, read_file


__all__ = [
    "env_reader",
    "environ_reader",
    "json_reader",
    "toml_reader",
    "yaml_reader",
]


def literal_eval(val: str) -> str | int | float | bool | list | dict:
    """Evaluate the string and return the literal"""

    return_val = None

    try:
        return_val = ast_literal_eval(val)
    except (ValueError, SyntaxError) as error:
        if isinstance(error, SyntaxError):
            if error.msg == "invalid decimal literal":
                return_val = str(val)
        else:
            return_val = str(val)

    return return_val


def env_reader(path: Path | PathLike | str) -> dict:
    """Read the environment variable strings from a file"""

    vars_ = {}
    for var, val in dotenv_values(path).items():

        if val is None:
            val = ""

        vars_[var] = literal_eval(val)

    return vars_


def environ_reader(vars_to_get: list[str]) -> dict:
    """Read the environment variable strings from os environment namespace"""

    vars_ = {var: environ[var] for var in vars_to_get}

    for var, val in vars_.items():

        # Check if the variable is declared in the environment
        EnvironVarUndeclaredError(var, val).check()

        vars_[var] = literal_eval(val)

    return vars_


def json_reader(path: Path | PathLike | str) -> dict:
    """Read the environment variable strings from a JSON file"""
    return json_reads(read_file(path))


def toml_reader(path: Path | PathLike | str) -> dict:
    """Read the environment variable strings from a TOML file"""
    return toml_reads(read_file(path))


def yaml_reader(path: Path | PathLike | str) -> dict:
    """Read the environment variable strings from a YAML file"""
    return yaml_reads(read_file(path))
