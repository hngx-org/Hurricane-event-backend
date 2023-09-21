from sqlalchemy import Column, String
from sqlalchemy import ForeignKey, Table
from models.basemodel import Base


comment_likes = Table("comment_likes",
                      Base.metadata,
                      Column("user_id", String(60),
                             ForeignKey("users.id")),
                      Column("comment_id", String(60),
                             ForeignKey("comments.id"))
                      )
