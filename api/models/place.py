from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Place(Base):
    __tablename__ = 'places'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(1024))
    
    visited = relationship('Visited', back_populates='place')
    
    
class Visited(Base):
    __tablename__ = 'visited'
    
    id = Column(Integer, ForeignKey('places.id'), primary_key=True)
    
    place = relationship('Place', back_populates='visited')
    