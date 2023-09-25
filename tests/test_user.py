import unittest
import json
import uuid
from models.user import User
from models.event import Event
from models.group import Group
from datetime import datetime
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
        self.unique_title = f'test-{uuid.uuid4()}-title'
        self.unique_email = f'test-{uuid.uuid4()}@example.com'
        self.udate = str((datetime.utcfromtimestamp(
            ((uuid.uuid4()).time - 0x01b21dd213814000) / 1e7)).strftime('%Y-%m-%d'))
        self.utime = str((datetime.utcfromtimestamp(
            ((uuid.uuid4()).time - 0x01b21dd213814000) / 1e7)).strftime('%H:%M:%S'))
        self.storage = DBStorage()
        self.storage.load()

    def test_authenticate_user_success(self):
        """ 
        Sucessfully authenticates user and returns user_id
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        test_data = {
            "email": self.unique_email, "name": "Test User", "avatar": "avatar.jpg"
        }

        response = self.client.post(
            '/api/auth', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertIn('user_id', data)
        self.assertEqual(response.status_code, 201)
        print(data)

    def test_authenticate_user_failure(self):
        """
        Fails to authenticate user with missing email
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        test_data = {
            "name": "Test User", "avatar": "avatar.jpg"
        }

        response = self.client.post(
            '/api/auth', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 412)
        self.assertEqual(data["message"], "No email found")
        print(data)

    def test_authenticate_user_failure2(self):
        """ 
        Fails to authenticate user with invalid email and missing name
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        test_data = {
            "email": "Invalid", "avatar": "avatar.jpg"
        }

        response = self.client.post(
            '/api/auth', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 412)
        self.assertEqual(data["message"], "No name found")
        print(data)

    def test_retrieve_user_success(self):
        """ 
        Successfully returns a user resource 
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        response = self.client.get(
            f'/api/users/{user.id}', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        print(data)

    def test_retrieve_user_failure(self):
        """ 
        Fails to return a user resource
        """
        response = self.client.get(
            '/api/users/1', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "User ID does not exist")
        print(data)

    def test_update_user_success(self):
        """ 
        Successfully updates a user resource
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        test_data = {
            "email": self.unique_email
        }

        response = self.client.put(
            f'/api/users/{user.id}', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 202)
        self.assertEqual(data["message"], "Update was successful")
        print(data)

    def test_update_user_unchanged(self):
        """ 
        Successfully updates a user resource with unchanged state
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        test_data = {
            "email": ""
        }

        response = self.client.put(
            f'/api/users/{user.id}', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "Unchanged")
        print(data)

    def test_update_user_failure(self):
        """
        Fails to update a user resource
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        test_data = {
            "email": self.unique_email
        }

        response = self.client.put(
            '/api/users/1', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "User ID does not exist")
        print(data)
        
    def test_add_event_user_success(self):
        """ 
        Successfully add an event to a user resource
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
        
        response = self.client.post(
            f'/api/users/{user.id}/interests/{event.id}', content_type='application/json')
        
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "success")
        
    def test_add_event_user_failure(self):
        """ 
        Fails to add an event to a user resource with invalid user ID
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
        
        response = self.client.post(
            f'/api/users/1/interests/{event.id}', content_type='application/json')
        
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid User ID")
        
    def test_add_event_user_failure2(self):
        """ 
        Fails to add an event to a user resource with invalid event ID
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        
        response = self.client.post(
            f'/api/users/{user.id}/interests/1', content_type='application/json')
        
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid Event ID")
        
    def test_remove_event_user_success(self):
        """ 
        Successfully removes an event to a user resource
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
            f'/api/users/{user.id}/interests/{event.id}', content_type='application/json')
        
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "success")
        
    def test_remove_event_user_failure(self):
        """ 
        Fails to remove an event to a user resource with invalid user ID
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
            f'/api/users/1/interests/{event.id}', content_type='application/json')
        
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid User ID")
        
    def test_remove_event_user_failure2(self):
        """ 
        Fails to add an event to a user resource with invalid event ID
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        
        response = self.client.delete(
            f'/api/users/{user.id}/interests/1', content_type='application/json')
        
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid Event ID")
        
    def test_invite_user_group_success(self):
        """ 
        Successfully invites users to a group
        """
        main_user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        main_user.save()
        group = Group(title=self.unique_title)
        group.save()
        
        test_data = {
            "users": [main_user.email]
        }
        
        response = self.client.post(
            f'/api/users/{main_user.id}/groups/{group.id}', data=json.dumps(test_data), content_type='application/json')
        
        data = json.loads(response.data.decode('utf-8'))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "success")
        self.assertEqual(type(data["added_users"]), list)
        self.assertEqual(type(data["invalid_users"]), list)
        print(data)
        
    def test_invite_user_group_failure(self):
        """ 
        Fails to invite users to a group with invalid user ID
        """
        main_user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        main_user.save()
        group = Group(title=self.unique_title)
        group.save()
        
        test_data = {
            "users": [main_user.email]
        }
        
        response = self.client.post(
            f'/api/users/1/groups/{group.id}', data=json.dumps(test_data), content_type='application/json')
        
        data = json.loads(response.data.decode('utf-8'))
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid User ID")
        print(data)
        
    def test_invite_user_group_failure2(self):
        """ 
        Fails to invite users to a group with invalid group ID
        """
        main_user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        main_user.save()
        
        test_data = {
            "users": [main_user.email]
        }
        
        response = self.client.post(
            f'/api/users/{main_user.id}/groups/1', data=json.dumps(test_data), content_type='application/json')
        
        data = json.loads(response.data.decode('utf-8'))
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid Group ID")
        print(data)
        
    def test_invite_user_group_failure3(self):
        """ 
        Fails to invite users to a group with missing users data
        """
        main_user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        main_user.save()
        group = Group(title=self.unique_title)
        group.save()
        
        test_data = {
        }
        
        response = self.client.post(
            f'/api/users/{main_user.id}/groups/{group.id}', data=json.dumps(test_data), content_type='application/json')
        
        data = json.loads(response.data.decode('utf-8'))
        
        self.assertEqual(response.status_code, 412)
        self.assertEqual(data["message"], "Users must be passed")
        print(data)
        

    def tearDown(self):
        """
        Teardown method to clean up after each test.
        """
        self.storage.close()


if __name__ == '__main__':
    unittest.main()