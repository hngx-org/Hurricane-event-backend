import unittest
from models.comment import Comment
from models.event import Event
from models.group import Group
from models.Image import Image
import models

class TestORM(unittest.TestCase):

    def set_up(self):
        self.app = create_app(config_name="testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tear_down(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_objects(self):

        user = user = User(name="test", email="", access_token="", refresh_token="", avatar="")# where do i get these tokens man :(
        user.save()
        self.assertIsNotNone(user.id) # just to make sure user has an id :)

        comment = Comment(body="", user_id="", event_id="")
        comment.save()
        self.assertIsNotNone(user.id) # again, just to make sure comment has an id :) 
        self.assertIsNotNone(event.id) # again, just to make sure comment has an id :) 

        event = event = Event(title="", description="", location="", start_date="", end_date="", start_time="", end_time="", thumnail="", creator_id="")
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
        user = User(name="Alice", email="alice@example.com")
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