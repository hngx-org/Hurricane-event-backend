import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from models.comment import Comment
from models.event import Event
from models.group import Group
from models.image import Image
import models

class TestORM(unittest.TestCase):

    def set_up(self):
        #setting up the test environment properly :)
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'our_test_database.db' # test db uri goes here :)
        db = SQLAlchemy(self.app) # init sqlalchemy, db defined :)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tear_down(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_objects(self):

        user = User(name="test", email="test@gmail.com", avatar="")
        user.save()
        self.assertIsNotNone(user.id) # just to make sure user has an id :)

        comment = Comment(body="", user_id="", event_id="")
        comment.save()
        self.assertIsNotNone(user.id) # again, just to make sure comment has an id :) 
        self.assertIsNotNone(event.id) # again, just to make sure comment has an id :) 

        start_date = datetime(2023, 9, 21).isoformat()
        end_date = datetime(2023, 9, 22).isoformat()
        start_time = datetime(2023, 9, 21, 8, 0, 0).isoformat()
        end_time = datetime(2023, 9, 21, 17, 0, 0).isoformat()


        event = Event(
            title="Sample Event",
            description="Event Description",
            location="Event Location",
            start_date=start_date,
            end_date=end_date,
            start_time=start_time,
            end_time=end_time,
            creator_id=user.id,  # Set the creator_id to the user's ID :)
        )
        event.save()
        self.assertIsNotNone(event.id) # same  reason as other two above :)
        self.assertIsNotNone(creator.id)

        group = group = Group(title="sample_title")
        group.save()
        self.assertIsNotNone(group.id)

        image = Image(image_url="")
        image.save()
        self.assertIsNotNone(image.id)

    def test_query_database(self):
        # Test querying the database for objects
        user = User(name="test", email="test@example.com")
        user.save()

        # Test getting all objects
        all_objects = models.storage.all()
        self.assertTrue(all_objects) 

        
        users = models.storage.all(User)
        self.assertTrue(users)

        # Test getting an object by ID
        retrieved_user = models.storage.get(User, id=user.id)
        self.assertEqual(retrieved_user.id, user.id)


if __name__ == "__main__":
    unittest.main()    
