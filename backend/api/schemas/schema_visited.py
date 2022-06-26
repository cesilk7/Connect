from pydantic import BaseModel


class VisitedResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True
