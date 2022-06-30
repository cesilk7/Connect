from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas import schema_visited
from api.cruds import crud_visited
from api.database import get_db


router = APIRouter()


@router.put('/places/{place_id}/visited', response_model=schema_visited.VisitedResponse)
async def mark_place_as_visited(place_id: int, db: AsyncSession = Depends(get_db)):
    visited = await crud_visited.get_visited(db, place_id=place_id)
    if visited is not None:
        raise HTTPException(status_code=400, detail='Visited already exists')

    return await crud_visited.create_visited(db, place_id)


@router.delete('/places/{place_id}/visited', response_model=None)
async def unmark_place_as_visited(place_id: int, db: AsyncSession = Depends(get_db)):
    visited = await crud_visited.get_visited(db, place_id=place_id)
    if visited is None:
        raise HTTPException(status_code=404, detail='Visited not found')

    return await crud_visited.delete_visited(db, original=visited)
