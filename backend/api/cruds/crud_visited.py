from typing import Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import model_visited


async def get_visited(db: AsyncSession, place_id: int) -> Optional[model_visited.Visited]:
    result: Result = await db.execute(
        select(model_visited.Visited).filter(model_visited.Visited.id == place_id)
    )
    visited: Optional[Tuple[model_visited.Visited]] = result.first()
    return visited[0] if visited is not None else None


async def create_visited(db: AsyncSession, place_id: int) -> model_visited.Visited:
    visited = model_visited.Visited(id=place_id)
    db.add(visited)
    await db.commit()
    await db.refresh(visited)
    return visited


async def delete_visited(db: AsyncSession, original: model_visited.Visited) -> None:
    await db.delete(original)
    await db.commit()
