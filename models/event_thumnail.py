from sqlalchemy import Column, String
from sqlalchemy import ForeignKey, Table
from models.basemodel import Base


event_thumnail = Table("event_thumbnail",
                       Base.metadata,
                       Column("image_id", String(60),
                              ForeignKey("images.id")),
                       Column("event_id", String(60),
                              ForeignKey("events.id"))
                       )
