"""Database Engine"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.basemodel import Base
from models.comment import Comment
from models.event import Event
from models.group import Group
from models.image import Image
from models.user import User

classes = {"Comment": Comment, "Event": Event, "Group": Group,
           "Image": Image, "User": User}


class DBStorage:
    """Database Class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes Database object"""
        DB_USER = getenv("DB_USER")
        DB_PASS = getenv("DB_PASS")
        DB_HOST = getenv("DB_HOST")
        DB_PORT = getenv("DB_PORT")

        self.__engine = create_engine("sqlite:///sampleEVENTAPP.db")

    def load(self):
        """Loads data from the database to session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def new(self, obj: Comment | Event | Group | Image | User):
        """Adds a new object to the session

        Args:
            obj (Comment | Event | Group | Image | User): Object to be added
        """
        self.__session.add(obj)
        self.save()

    def save(self):
        """Saves all objects in session to the database"""
        self.__session.commit()

    def all(self, cls: Comment | Event | Group | Image | User | str = None):
        """Gets all instances of a model in session
        Args:
            cls (Comment | Event | Group | Image | User | str): Model to query
        Returns:
            list: A list of all the instances in the session
        """
        if type(cls) is str:
            cls = classes.get(cls)
        if cls is not None and cls not in classes.values():
            return self.__session.query(cls).all()
        objects = []
        for cls in classes.values():
            objects.extend(self.__session.query(cls).all())
        return objects

    def get(self, cls: Comment | Event | Group | Image | User | str, id: str):
        """Gets an instance of a model
        Args:
            cls (Comment | Event | Group | Image | User | str): Model to query
        Returns:
            (Comment | Event | Group | Image | User): Instance of the model
        """
        if type(cls) is str:
            cls = classes.get(cls)
        if cls is not None and cls in classes.values():
            return self.__session.query(cls).filter_by(id=id).first()

    def getUser(self, cls: Comment | Event | Group | Image | User | str, id: str):
        """Gets an instance of a User
            Only use during login to verify user details
        """
        if type(cls) is str:
            cls = classes.get(cls)
        if cls is not None and cls in classes.values():
            return self.__session.query(cls).filter_by(email=id).first()
        
    def getImages(self, cls: Comment | Event | Group | Image | User | str, id: str):
        """
        Get all images associated with a given comment
        """
        if type(cls) is str:
            cls = classes.get(cls)
        if cls is not None and cls in classes.values():
            return self.__session.query(cls).filter_by(comment_id=id).all()

    def close(self):
        """Closes the session connection"""
        self.__session.remove()

    def delete(self, cls: Comment | Event | Group | Image | User | str,
               id: str) -> None:
        """Deletes an instance of the model from the database using id"""

        if type(cls) is str:
            cls = classes.get(cls)
        if cls is not None and cls in classes.values():
            inst = self.__session.query(cls).filter_by(id=id).first()
            self.__session.delete(inst)

    def obj_delete(self, obj: Comment | Event | Group | Image | User):
        """Deletes an instance of the model from the database"""
        self.__session.delete(obj)
