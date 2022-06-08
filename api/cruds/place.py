from typing import List, Tuple, Optional

import api.models.place as place_model
import api.schemas.place as place_schema
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


async def create_place(
    db: AsyncSession, place_create: place_schema.PlaceCreate
) -> place_model.Place:
    place = place_model.Place(**place_create.dict())
    db.add(place)
    await db.commit()
    await db.refresh(place)
    return place


async def get_places_with_visited(db: AsyncSession) -> List[Tuple[int, str, bool]]:
    result: Result = await (
        db.execute(
            select(
                place_model.Place.id,
                place_model.Place.name,
                place_model.Visited.id.isnot(None).label('visited'),
            ).outerjoin(place_model.Visited)
        )
    )
    return result.all()


async def get_place(db: AsyncSession, place_id: int) -> Optional[place_model.Place]:
    result: Result = await db.execute(
        select(place_model.Place).filter(place_model.Place.id == place_id)
    )
    place: Optional[Tuple[place_model.Place]] = result.first()
    return place[0] if place is not None else None


async def update_place(
    db: AsyncSession, place_create: place_schema.PlaceCreate, original: place_model.Place
) -> place_model.Place:
    original.name = place_create.name
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_place(db: AsyncSession, original: place_model.Place) -> None:
    await db.delete(original)
    await db.commit()
