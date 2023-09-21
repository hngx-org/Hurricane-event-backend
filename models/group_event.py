from sqlalchemy import Column, String
from sqlalchemy import ForeignKey, Table
from models.basemodel import Base


group_events = Table("group_events",
                     Base.metadata,
                     Column("event_id", String(60), ForeignKey("events.id")),
                     Column("group_id", String(60), ForeignKey("groups.id"))
                     )