from typing import Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import model_place


async def get_visited(db: AsyncSession, place_id: int) -> Optional[model_place.Visited]:
    result: Result = await db.execute(
        select(model_place.Visited).filter(model_place.Visited.id == place_id)
    )
    visited: Optional[Tuple[model_place.Visited]] = result.first()
    return visited[0] if visited is not None else None


async def create_visited(db: AsyncSession, place_id: int) -> model_place.Visited:
    visited = model_place.Visited(id=place_id)
    db.add(visited)
    await db.commit()
    await db.refresh(visited)
    return visited


async def delete_visited(db: AsyncSession, original: model_place.Visited) -> None:
    await db.delete(original)
    await db.commit()
