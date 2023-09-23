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

    def test_login_success(self):
        """
        Successfully login user
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        payload = {
            "userinfo": {
                "email": user.email,
                "name": "Test User",
                "picture": "https://example.com/avatar.jpg"
            }
        }

        response = self.client.post(
            '/api/users/login', data=json.dumps(payload))

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn("user_id", data)
        self.assertIn("name", data)
        self.assertIn("email", data)
        self.assertIn("avatar", data)
        print(data)

    def test_login_no_result(self):
        """ 
        Create new user if user not found
        """
        payload = {
            "userinfo": {
                "email": self.unique_email,
                "name": "Test User",
                "picture": "https://example.com/avatar.jpg"
            }
        }

        response = self.client.post(
            '/api/users/login', data=json.dumps(payload))

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn("user_id", data)
        self.assertIn("name", data)
        self.assertIn("email", data)
        self.assertIn("avatar", data)
        print(data)

    def tearDown(self):
        """
        Teardown method to clean up after each test.
        """
        self.storage.close()


if __name__ == '__main__':
    unittest.main()
