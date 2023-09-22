import unittest
import json
import uuid
from datetime import datetime
from models.event import Event
from models.comment import Comment
from models.user import User
from app import app
from models.engine.database import DBStorage


class TestViewsUser(unittest.TestCase):
    def setUp(self):
        """
        Setup method to configure the testing environment.
        """
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.unique_id = str(uuid.uuid4())
        self.unique_email = f'test-{uuid.uuid4()}@example.com'
        self.udate = str((datetime.utcfromtimestamp(
            ((uuid.uuid4()).time - 0x01b21dd213814000) / 1e7)).strftime('%Y-%m-%d'))
        self.utime = str((datetime.utcfromtimestamp(
            ((uuid.uuid4()).time - 0x01b21dd213814000) / 1e7)).strftime('%H:%M:%S'))
        self.storage = DBStorage()
        self.storage.load()

    def test_add_comment_event_success(self):
        """ 
        Successfully adds a comment to an event
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        event = Event(
            title="test_title",
            description="test_description",
            location="test_location",
            start_date=self.udate,
            end_date=self.udate,
            start_time=self.utime,
            end_time=self.utime,
            creator_id=user.id,
            thumbnail="thumbnail.jpg"
        )
        event.save()
        test_data = {
            "body": "test_body",
            "user_id": user.id,
            "image": "image.jpg"
        }

        response = self.client.post(
            f'/api/events/{event.id}/comments', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["message"], "success")
        print(data)

    def test_add_comment_event_failure(self):
        """ 
        Fails to add a comment to an event with invalid event ID
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        test_data = {
            "body": "test_body",
            "user_id": user.id,
            "image": "image.jpg"
        }

        response = self.client.post(
            '/api/events/1/comments', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid Event ID")
        print(data)

    def test_add_comment_event_failure2(self):
        """ 
        Fails to add a comment to an event with missing body
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        event = Event(
            title="test_title",
            description="test_description",
            location="test_location",
            start_date=self.udate,
            end_date=self.udate,
            start_time=self.utime,
            end_time=self.utime,
            creator_id=user.id,
            thumbnail="thumbnail.jpg"
        )
        event.save()
        comment = Comment(body="test_body", user_id=user.id, event_id=event.id)
        comment.save()
        test_data = {
            "user_id": user.id,
            "image": "image.jpg"
        }

        response = self.client.post(
            f'/api/events/{event.id}/comments', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 412)
        self.assertEqual(data["message"], "Incomplete comment details")
        print(data)

    def test_add_comment_event_failure3(self):
        """ 
        Fails to add a comment to an event with missing user ID
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        event = Event(
            title="test_title",
            description="test_description",
            location="test_location",
            start_date=self.udate,
            end_date=self.udate,
            start_time=self.utime,
            end_time=self.utime,
            creator_id=user.id,
            thumbnail="thumbnail.jpg"
        )
        event.save()
        test_data = {
            "body": "test_body",
            "image": "image.jpg"
        }

        response = self.client.post(
            f'/api/events/{event.id}/comments', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 412)
        self.assertEqual(data["message"], "Incomplete comment details")
        print(data)

    def test_retrieve_comments_event_success(self):
        """ 
        Successfully returns list of comments of an event
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        event = Event(
            title="test_title",
            description="test_description",
            location="test_location",
            start_date=self.udate,
            end_date=self.udate,
            start_time=self.utime,
            end_time=self.utime,
            creator_id=user.id,
            thumbnail="thumbnail.jpg"
        )
        event.save()
        comment = Comment(body="test_comment",
                          user_id=user.id, event_id=event.id)
        comment.save()

        response = self.client.get(
            f'/api/events/{event.id}/comments', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        print(data)

    def test_retrieve_comments_event_failure(self):
        """ 
        Fails to return list of comments of an event with invalid event ID
        """
        response = self.client.get(
            '/api/events/1/comments', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid Event ID")
        print(data)

    def test_add_image_comment_success(self):
        """ 
        Successfully adds an image to a comment
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        event = Event(
            title="test_title",
            description="test_description",
            location="test_location",
            start_date=self.udate,
            end_date=self.udate,
            start_time=self.utime,
            end_time=self.utime,
            creator_id=user.id,
            thumbnail="thumbnail.jpg"
        )
        event.save()
        comment = Comment(body="test_comment",
                          user_id=user.id, event_id=event.id)
        comment.save()

        test_data = {
            "image": "image.jpg"
        }

        response = self.client.post(
            f'/api/comments/{comment.id}/images', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["message"], "success")
        print(data)

    def test_add_image_comment_failure(self):
        """ 
        Fails to add an image to a comment with missing image
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        event = Event(
            title="test_title",
            description="test_description",
            location="test_location",
            start_date=self.udate,
            end_date=self.udate,
            start_time=self.utime,
            end_time=self.utime,
            creator_id=user.id,
            thumbnail="thumbnail.jpg"
        )
        event.save()
        comment = Comment(body="test_comment",
                          user_id=user.id, event_id=event.id)
        comment.save()

        test_data = {
        }

        response = self.client.post(
            f'/api/comments/{comment.id}/images', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 412)
        self.assertEqual(data["message"], "Image url was not passed")
        print(data)

    def test_add_image_comment_failure2(self):
        """ 
        Fails to add an image to a comment with invalid comment id
        """
        test_data = {
        }

        response = self.client.post(
            '/api/comments/1/images', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid Comment ID")
        print(data)

    def test_retrieve_image_comment_success(self):
        """ 
        Successfully returns an image from a comment
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        event = Event(
            title="test_title",
            description="test_description",
            location="test_location",
            start_date=self.udate,
            end_date=self.udate,
            start_time=self.utime,
            end_time=self.utime,
            creator_id=user.id,
            thumbnail="thumbnail.jpg"
        )
        event.save()
        comment = Comment(body="test_comment",
                          user_id=user.id, event_id=event.id)
        comment.save()

        response = self.client.get(
            f'/api/comments/{comment.id}/images', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        print(data)

    def test_retrieve_image_comment_failure(self):
        """ 
        Fails to return an image from a comment with invalid comment ID
        """
        response = self.client.get(
            '/api/comments/1/images', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid Comment ID")
        print(data)

    def tearDown(self):
        """
        Teardown method to clean up after each test.
        """
        self.storage.close()


if __name__ == '__main__':
    unittest.main()
