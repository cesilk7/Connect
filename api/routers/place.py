from typing import List

from fastapi import APIRouter

import api.schemas.place as place_schema


router = APIRouter()


@router.get('/places', response_model=List[place_schema.Place])
async def list_place():
    return [place_schema.Place(id=1, name='スパラクーア')]


@router.post('/places', response_model=place_schema.PlaceCreateResponse)
async def create_place(place_body: place_schema.PlaceCreate):
    return place_schema.PlaceCreateResponse(id=1, **place_body.dict())


@router.put('/places/{place_id}', response_model=place_schema.PlaceCreateResponse)
async def update_place(place_id: int, place_body: place_schema.PlaceCreate):
    return place_schema.PlaceCreateResponse(id=place_id, **place_body.dict())


@router.delete('/places/{place_id}', response_model=None)
async def delete_place(place_id: int):
    return
