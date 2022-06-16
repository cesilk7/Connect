from typing import List

import api.cruds.place as place_crud
import api.schemas.place as place_schema
from api.db import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get('/places', response_model=List[place_schema.Place])
async def list_place(db: AsyncSession = Depends(get_db)):
    return await place_crud.get_places_with_visited(db)


@router.post('/places', response_model=place_schema.PlaceCreateResponse)
async def create_place(place_body: place_schema.PlaceCreate, db: AsyncSession = Depends(get_db)):
    return await place_crud.create_place(db, place_body)


@router.put('/places/{place_id}', response_model=place_schema.PlaceCreateResponse)
async def update_place(
    place_id: int, place_body: place_schema.PlaceCreate, db: AsyncSession = Depends(get_db)
):
    place = await place_crud.get_place(db, place_id=place_id)
    if place is None:
        raise HTTPException(status_code=404, detail='Place not found')

    return await place_crud.update_place(db, place_body, original=place)


@router.delete('/places/{place_id}', response_model=None)
async def delete_place(place_id: int, db: AsyncSession = Depends(get_db)):
    place = await place_crud.get_place(db, place_id=place_id)
    if place is None:
        raise HTTPException(status_code=404, detail='Place not found')

    return await place_crud.delete_place(db, original=place)
