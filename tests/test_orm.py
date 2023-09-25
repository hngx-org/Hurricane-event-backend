import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models.user import User
from models.comment import Comment
from models.event import Event
from models.group import Group
from models.image import Image
import models, uuid

class TestORM(unittest.TestCase):

    def setUp(self):
        #setting up the test environment properly :)
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///testEVENTAPP.db" # test db uri goes here :)
        self.db = SQLAlchemy(self.app) # init sqlalchemy, db defined :)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db.create_all()
        

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()

    def test_create_objects(self):

        user = User(name="test", email=f'test-{uuid.uuid4()}@example.com', avatar="")
        user.save()
        self.assertIsNotNone(user.id) # just to make sure user has an id :)
        
        start_date = datetime(2023, 9, 21).strftime('%Y-%m-%d')
        end_date = datetime(2023, 9, 22).strftime('%Y-%m-%d')
        start_time = datetime(2023, 9, 21, 8, 0, 0).strftime('%H:%M:%S')
        end_time = datetime(2023, 9, 21, 17, 0, 0).strftime('%H:%M:%S')
        
        event = Event(
            title="Sample Event",
            description="Event Description",
            location="Event Location",
            start_date=start_date,
            end_date=end_date,
            start_time=start_time,
            end_time=end_time,
            creator_id=user.id,  # Set the creator_id to the user's ID :)
            thumbnail="thumbnail.jpg"
        )
        event.save()
        self.assertIsNotNone(event.id) # same  reason as other two above :)
        self.assertIsNotNone(event.creator_id)

        comment = Comment(body="", user_id="", event_id="")
        comment.save()
        self.assertIsNotNone(user.id) # again, just to make sure comment has an id :) 
        self.assertIsNotNone(event.id) # again, just to make sure comment has an id :) 

        group = group = Group(title=f'test-{uuid.uuid4()}-title')
        group.save()
        self.assertIsNotNone(group.id)

        image = Image(image_url="")
        image.save()
        self.assertIsNotNone(image.id)

    def test_query_database(self):
        # Test querying the database for objects
        user = User(name="test", email=f'test-{uuid.uuid4()}@example.com', avatar="")
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
