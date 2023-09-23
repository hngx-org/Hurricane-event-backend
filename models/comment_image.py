from sqlalchemy import Column, String
from sqlalchemy import ForeignKey, Table
from models.basemodel import Base


comment_image = Table("comment_image",
                      Base.metadata,
                      Column("image_id", String(60),
                             ForeignKey("images.id")),
                      Column("comment_id", String(60),
                             ForeignKey("comments.id"))
                      )
