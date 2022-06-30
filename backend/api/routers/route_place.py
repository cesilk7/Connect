from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.cruds import crud_place
from api.schemas import schema_place
from api.database import get_db

router = APIRouter()


@router.get('/places', response_model=List[schema_place.Place])
async def list_place(db: AsyncSession = Depends(get_db)):
    return await crud_place.get_places_with_visited(db)


@router.post('/places', response_model=schema_place.PlaceCreateResponse)
async def create_place(place_body: schema_place.PlaceCreate, db: AsyncSession = Depends(get_db)):
    return await crud_place.create_place(db, place_body)


@router.put('/places/{place_id}', response_model=schema_place.PlaceCreateResponse)
async def update_place(
    place_id: int, place_body: schema_place.PlaceCreate, db: AsyncSession = Depends(get_db)
):
    place = await crud_place.get_place(db, place_id=place_id)
    if place is None:
        raise HTTPException(status_code=404, detail='Place not found')

    return await crud_place.update_place(db, place_body, original=place)


@router.delete('/places/{place_id}', response_model=None)
async def delete_place(place_id: int, db: AsyncSession = Depends(get_db)):
    place = await crud_place.get_place(db, place_id=place_id)
    if place is None:
        raise HTTPException(status_code=404, detail='Place not found')

    return await crud_place.delete_place(db, original=place)
