from sqlalchemy import Column, String
from sqlalchemy import ForeignKey, Table
from models.basemodel import Base


group_image = ""
# group_image = Table("group_image",
#                     Base.metadata,
#                     Column("image_id", String(60),
#                            ForeignKey("images.id")),
#                     Column("group_id", String(60),
#                            ForeignKey("events.id"))
#                     )
