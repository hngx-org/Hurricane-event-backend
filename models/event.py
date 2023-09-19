"""Model for Event table"""
from datetime import date, datetime
from sqlalchemy import Column, String, Date, DateTime
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

group_events = Table("group_events",
                     Base.metadata,
                     Column("event_id", String(60), ForeignKey("events.id")),
                     Column("group_id", String(60), ForeignKey("groups.id"))
                     )

interested_events = Table("interested_events",
                          Base.metadata,
                          Column("user_id", String(60),
                                 ForeignKey("users.id")),
                          Column("event_id", String(60),
                                 ForeignKey("events.id"))
                          )


class Event(BaseModel, Base):
    """Event Class"""

    __tablename__ = "events"
    title = Column(String(60))
    description = Column(String(1024), nullable=True)
    location = Column(String(1024))
    start_date = Column(Date)
    end_date = Column(Date)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    thumbnail = Column(String(255), nullable=True)
    creator_id = Column(String(60), ForeignKey("users.id"))
    groups = relationship("Group", secondary=group_events,
                          back_populates="events")
    users = relationship("User", secondary=interested_events,
                         back_populates="events")

    def __init__(self, title: str, description: str, location: str,
                 start_date: date, end_date: Date, start_time: datetime,
                 end_time: datetime, thumnail: str, creator_id: str):
        """Initializes the event class"""
        self.title = title
        self.description = description
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.thumbnail = thumnail
        self.creator_id = creator_id
