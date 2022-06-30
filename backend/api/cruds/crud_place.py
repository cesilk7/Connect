from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import model_place, model_visited
from api.schemas import schema_place


async def create_place(
    db: AsyncSession, place_create: schema_place.PlaceCreate
) -> model_place.Place:
    place = model_place.Place(**place_create.dict())
    db.add(place)
    await db.commit()
    await db.refresh(place)
    return place


async def get_places_with_visited(db: AsyncSession) -> List[Tuple[int, str, bool]]:
    result: Result = await (
        db.execute(
            select(
                model_place.Place.id,
                model_place.Place.name,
                model_visited.Visited.id.isnot(None).label('visited'),
            ).outerjoin(model_visited.Visited)
        )
    )
    return result.all()


async def get_place(db: AsyncSession, place_id: int) -> Optional[model_place.Place]:
    result: Result = await db.execute(
        select(model_place.Place).filter(model_place.Place.id == place_id)
    )
    place: Optional[Tuple[model_place.Place]] = result.first()
    return place[0] if place is not None else None


async def update_place(
    db: AsyncSession, place_create: schema_place.PlaceCreate, original: model_place.Place
) -> model_place.Place:
    original.name = place_create.name
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_place(db: AsyncSession, original: model_place.Place) -> None:
    await db.delete(original)
    await db.commit()
