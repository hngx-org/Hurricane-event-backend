from sqlalchemy import Column, String
from sqlalchemy import ForeignKey, Table
from models.basemodel import Base


interested_events = Table("interested_events",
                          Base.metadata,
                          Column("user_id", String(60),
                                 ForeignKey("users.id")),
                          Column("event_id", String(60),
                                 ForeignKey("events.id"))
                          )
