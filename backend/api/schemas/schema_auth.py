from typing import Union

from decouple import config
from pydantic import BaseModel, Field

CSRF_KEY = config('CSRF_KEY')


class CsrfSettings(BaseModel):
    secret_key: str = CSRF_KEY


class SuccessMsg(BaseModel):
    message: str


class User(BaseModel):
    id: int
    name: Union[str, None] = None
    email: str

    class Config:
        orm_mode = True


class UserBody(BaseModel):
    email: str
    password: str


class Csrf(BaseModel):
    csrf_token: str
