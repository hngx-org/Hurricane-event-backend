from sqlalchemy import Column, String, Table, ForeignKey
from models.basemodel import Base


user_groups = Table("user_groups",
                    Base.metadata,
                    Column("user_id", String(60), ForeignKey("users.id")),
                    Column("group_id", String(60), ForeignKey("groups.id"))
                    )