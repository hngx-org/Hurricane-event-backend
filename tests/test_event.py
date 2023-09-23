import unittest
import json
import uuid
from datetime import datetime
from models.event import Event
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
        self.unique_email = f'test-{uuid.uuid4()}@example.com'
        self.udate = str((datetime.utcfromtimestamp(
            ((uuid.uuid4()).time - 0x01b21dd213814000) / 1e7)).strftime('%Y-%m-%d'))
        self.utime = str((datetime.utcfromtimestamp(
            ((uuid.uuid4()).time - 0x01b21dd213814000) / 1e7)).strftime('%H:%M:%S'))
        self.storage = DBStorage()
        self.storage.load()

    def test_create_event_success(self):
        """ 
        Successfully creates new event
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        test_data = {
            "title": "test_title",
            "description": "test_description",
            "location": "test_location",
            "start_date": self.udate,
            "end_date": self.udate,
            "start_time": self.utime,
            "end_time": self.utime,
            "creator_id": user.id,
            "thumbnail": "thumbnail.jpg"
        }

        response = self.client.post(
            '/api/events', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        print(data)

    def test_create_event_failure(self):
        """ 
         Fails to create new event with invalid creator ID
         """
        test_data = {
            "title": "test_title",
            "description": "test_description",
            "location": "test_location",
            "start_date": self.udate,
            "end_date": self.udate,
            "start_time": self.utime,
            "creator_id": 1,
            "thumbnail": "thumbnail.jpg"
        }

        response = self.client.post(
            '/api/events', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "User not found")
        print(data)
        
    def test_create_event_failure2(self):
        """ 
         Fails to create new event
         """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        test_data = {
            "title": "test_title",
            "description": "test_description",
            "location": "test_location",
            "start_date": self.udate,
            "end_date": self.udate,
            "start_time": self.utime,
            "creator_id": user.id,
            "thumbnail": "thumbnail.jpg"
        }

        response = self.client.post(
            '/api/events', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 412)
        self.assertEqual(data["message"], "Incomplete event details")
        print(data)

    def test_retrieve_all_events(self):
        """ 
        Returns list of existing events
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

        response = self.client.get(
            '/api/events', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(data), list)
        print(data)

    def test_retrieve_event_success(self):
        """ 
        Successfully returns existing event by id
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

        response = self.client.get(
            f'/api/events/{event.id}', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        print(data)

    def test_retrieve_event_failure(self):
        """ 
        Fails to return existing event with invalid id
        """
        response = self.client.get(
            '/api/events/1', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Event not found")
        print(data)

    def test_update_event_success(self):
        """ 
        Successfully updates an event resource
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
            "end_date": self.udate
        }

        response = self.client.put(
            f'/api/events/{event.id}', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 202)
        self.assertEqual(data["message"], "success")
        print(data)

    def test_update_event_unchanged(self):
        """ 
        Successfully updates an event resource with unchanged state
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
            "location": ""
        }

        response = self.client.put(
            f'/api/events/{event.id}', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "unchanged")
        print(data)

    def test_update_event_failure(self):
        """
        Fails to update an event resource
        """
        test_data = {
            "location": "new_location"
        }

        response = self.client.put(
            '/api/events/1', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "User ID does not exist")
        print(data)

    def test_delete_event_success(self):
        """ 
        Successfully deletes an event by id
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

        response = self.client.delete(
            f'/api/events/{event.id}', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "success")
        print(data)

    def test_delete_event_failure(self):
        """ 
        Fails to delete an event by id
        """
        response = self.client.delete(
            '/api/events/1', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Resource UID not found")
        print(data)

    def test_retrieve_interested_events_success(self):
        """ 
        Successfully returns events a user is interested in 
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        response = self.client.get(
            f'/api/events/{user.id}/events', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('user', data)
        self.assertIn('events', data)
        print(data)

    def test_retrieve_interested_events_failure(self):
        """ 
        Fails to return events a user is interested in with invalid user ID
        """
        response = self.client.get(
            f'/api/events/1/events', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "User not found")
        print(data)

    def tearDown(self):
        """
        Teardown method to clean up after each test.
        """
        self.storage.close()


if __name__ == '__main__':
    unittest.main()