from typing import Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.place as place_model


async def get_visited(db: AsyncSession, place_id: int) -> Optional[place_model.Visited]:
    result: Result = await db.execute(
        select(place_model.Visited).filter(place_model.Visited.id == place_id)
    )
    visited: Optional[Tuple[place_model.Visited]] = result.first()
    return visited[0] if visited is not None else None


async def create_visited(db: AsyncSession, place_id: int) -> place_model.Visited:
    visited = place_model.Visited(id=place_id)
    db.add(visited)
    await db.commit()
    await db.refresh(visited)
    return visited


async def delete_visited(db: AsyncSession, original: place_model.Visited) -> None:
    await db.delete(original)
    await db.commit()
