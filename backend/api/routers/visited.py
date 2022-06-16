from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.visited as visited_schema
import api.cruds.visited as visited_crud
from api.db import get_db


router = APIRouter()


@router.put('/places/{place_id}/visited', response_model=visited_schema.VisitedResponse)
async def mark_place_as_visited(place_id: int, db: AsyncSession = Depends(get_db)):
    visited = await visited_crud.get_visited(db, place_id=place_id)
    if visited is not None:
        raise HTTPException(status_code=400, detail='Visited already exists')

    return await visited_crud.create_visited(db, place_id)


@router.delete('/places/{place_id}/visited', response_model=None)
async def unmark_place_as_visited(place_id: int, db: AsyncSession = Depends(get_db)):
    visited = await visited_crud.get_visited(db, place_id=place_id)
    if visited is None:
        raise HTTPException(status_code=404, detail='Visited not found')

    return await visited_crud.delete_visited(db, original=visited)
