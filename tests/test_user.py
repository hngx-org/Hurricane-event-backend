import unittest
import json
import uuid
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
        self.assertEqual(response.status_code, 200)
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

    def tearDown(self):
        """
        Teardown method to clean up after each test.
        """
        self.storage.close()


if __name__ == '__main__':
    unittest.main()