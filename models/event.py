"""Model for Event table"""
from datetime import date, time
from sqlalchemy import Column, String, Date, Time
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base
from models.group_event import group_events
from models.interested_event import interested_events
from models.event_thumnail import event_thumnail


class Event(BaseModel, Base):
    """Event Class"""

    __tablename__ = "events"
    title = Column(String(60))
    description = Column(String(1024), nullable=True)
    location = Column(String(1024))
    start_date = Column(Date)
    end_date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    creator_id = Column(String(60), ForeignKey("users.id"))
    thumbnail = Column(String(60), nullable=True)
    groups = relationship("Group", secondary=group_events,
                          back_populates="events")
    users = relationship("User", secondary=interested_events,
                         back_populates="events")
    # image = relationship("Image", secondary=event_thumnail, uselist=False)

    def __init__(self, title: str, description: str, location: str,
                 start_date: str, end_date: str, start_time: str,
                 end_time: str, thumbnail: str, creator_id: str):
        """Initializes the event class"""
        self.title = title
        self.description = description
        self.location = location
        self.start_date = date.fromisoformat(start_date)
        self.end_date = date.fromisoformat(end_date)
        self.start_time = time.fromisoformat(start_time)
        self.end_time = time.fromisoformat(end_time)
        self.thumbnail = thumbnail
        self.creator_id = creator_id

        super().__init__()
