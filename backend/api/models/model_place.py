from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.database import Base


class Place(Base):
    __tablename__ = 'places'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(1024))
    
    visited = relationship('Visited', back_populates='place')