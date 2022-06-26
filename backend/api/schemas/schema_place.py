from typing import Optional

from pydantic import BaseModel, Field


class PlaceBase(BaseModel):
    name: Optional[str] = Field(None, example='スパラクーア')


class PlaceCreate(PlaceBase):
    pass


class PlaceCreateResponse(PlaceBase):
    id: int

    class Config:
        orm_mode = True


class Place(PlaceBase):
    id: int
    visited: bool = Field(False, description='訪問済み')

    class Config:
        orm_mode = True
