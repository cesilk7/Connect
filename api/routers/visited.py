from fastapi import APIRouter


router = APIRouter()


@router.put('/places/{place_id}/visited', response_model=None)
async def mark_place_as_visited(place_id: int):
    return


@router.delete('/places/{place_id}/visited', response_model=None)
async def unmark_place_as_visited(place_id: int):
    return
