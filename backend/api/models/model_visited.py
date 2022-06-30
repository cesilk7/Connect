from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from api.database import Base


class Visited(Base):
    __tablename__ = 'visited'
    
    id = Column(Integer, ForeignKey('places.id'), primary_key=True)
    
    place = relationship('Place', back_populates='visited')
    