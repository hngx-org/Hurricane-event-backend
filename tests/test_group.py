import unittest
import json
import uuid
from models.group import Group
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
        self.unique_title = f'test-{uuid.uuid4()}-title'
        self.unique_email = f'test-{uuid.uuid4()}@example.com'
        self.storage = DBStorage()
        self.storage.load()

    def test_create_group_success(self):
        """Successfully creates new group
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        test_data = {
            "title": self.unique_title, "image": "test_image.png", "user_id": user.id
        }

        response = self.client.post(
            '/api/groups', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        print(data)

    def test_create_group_failure(self):
        """
        Fails to create new group with no title
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        test_data = {
            "image": "test_image.png", "user_id": user.id
        }

        response = self.client.post(
            '/api/groups', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 412)
        self.assertEqual(data["message"], "Title is required")
        print(data)
        
    def test_create_group_failure2(self):
        """
        Fails to create new group with no user ID
        """
        test_data = {
            "title": self.unique_title, "image": "test_image.png"
        }

        response = self.client.post(
            '/api/groups', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 412)
        self.assertEqual(data["message"], "User ID is required")
        print(data)

    def test_create_group_failure3(self):
        """
        Fails to create new group with existing title
        """
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()
        group = Group(title=self.unique_title)
        group.save()
        test_data = {
            "title": group.title, "image": "test_image.png", "user_id": user.id
        }

        response = self.client.post(
            '/api/groups', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 409)
        self.assertEqual(data["message"], f'Group with title "{group.title}" already exists')
        print(data)
        
    def test_create_group_failure4(self):
        """
        Fails to create new group with invalid user ID
        """
        test_data = {
            "title": self.unique_title, "image": "test_image.png", "user_id": 1
        }

        response = self.client.post(
            '/api/groups', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid User ID")
        print(data)

    def test_retrieve_group_success(self):
        """ 
        Successfully returns group by id
        """
        group = Group(title=self.unique_title)
        group.save()

        response = self.client.get(
            f'/api/groups/{group.id}', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        print(data)

    def test_retrieve_group_failure(self):
        """ 
        Fails to return group with invalid id
        """
        group = Group(title=self.unique_title)
        group.save()

        response = self.client.get(
            '/api/groups/1', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Group not found")
        print(data)

    def test_update_group_success(self):
        """ 
        Successfully updates a group resource
        """
        group = Group(title=self.unique_title)
        group.save()

        test_data = {
            "title": self.unique_title
        }

        response = self.client.put(
            f'/api/groups/{group.id}', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 202)
        self.assertEqual(data["message"], "success")
        print(data)

    def test_update_group_unchanged(self):
        """ 
        Successfully updates a group resource with unchanged state
        """
        group = Group(title=self.unique_title)
        group.save()

        test_data = {

        }

        response = self.client.put(
            f'/api/groups/{group.id}', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "unchanged")
        print(data)

    def test_update_group_failure(self):
        """
        Fails to update a group resource
        """
        test_data = {
            "title": self.unique_title
        }

        response = self.client.put(
            '/api/groups/1', data=json.dumps(test_data), content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid Group ID")
        print(data)

    def test_delete_group_success(self):
        """ 
        Successfully deletes a group by id
        """
        group = Group(title=self.unique_title)
        group.save()

        response = self.client.delete(
            f'/api/groups/{group.id}', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "success")
        print(data)

    def test_delete_group_failure(self):
        """ 
        Fails to delete a group by id
        """
        response = self.client.delete(
            '/api/groups/1', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid Group ID")
        print(data)

    def test_add_user_group_success(self):
        """ 
        Successfully adds a user to a group
        """
        group = Group(title=self.unique_title)
        group.save()
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        response = self.client.post(
            f'/api/groups/{group.id}/members/{user.id}', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "success")
        print(data)

    def test_add_user_group_failure(self):
        """ 
        Fails to add a user to a group with invalid user ID
        """
        group = Group(title=self.unique_title)
        group.save()
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        response = self.client.post(
            f'/api/groups/{group.id}/members/1', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid User ID")
        print(data)

    def test_add_user_group_failure2(self):
        """ 
        Fails to add a user to a group with invalid group ID
        """
        group = Group(title=self.unique_title)
        group.save()
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        response = self.client.post(
            f'/api/groups/1/members/{user.id}', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid Group ID")
        print(data)

    def test_remove_user_group_success(self):
        """ 
        Successfully removes a user from group
        """
        group = Group(title=self.unique_title)
        group.save()
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        self.client.post(
            f'/api/groups/{group.id}/members/{user.id}', content_type='application/json')

        response = self.client.delete(
            f'/api/groups/{group.id}/members/{user.id}', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "success")
        print(data)

    def test_remove_user_group_failure(self):
        """ 
        Fails to remove a user to a group with invalid user ID
        """
        group = Group(title=self.unique_title)
        group.save()
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        self.client.post(
            f'/api/groups/{group.id}/members/{user.id}', content_type='application/json')

        response = self.client.delete(
            f'/api/groups/{group.id}/members/1', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid User ID")
        print(data)

    def test_remove_user_group_failure2(self):
        """ 
        Fails to remove a user to a group with invalid group ID
        """
        group = Group(title=self.unique_title)
        group.save()
        user = User(name="Test User", email=self.unique_email,
                    avatar="avatar.jpg")
        user.save()

        self.client.post(
            f'/api/groups/{group.id}/members/{user.id}', content_type='application/json')

        response = self.client.delete(
            f'/api/groups/1/members/{user.id}', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid Group ID")
        print(data)
        
    def test_retrieve_group_event_success(self):
        """ 
        Successfully retrieves list of events in a group
        """
        group = Group(title=self.unique_title)
        group.save()

        response = self.client.get(
            f'/api/groups/{group.id}/events', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(data), list)
        print(data)

    def test_retrieve_group_event_failure(self):
        """ 
        Fails to retrieve list of events in a group
        """
        response = self.client.get(
            '/api/groups/1/events', content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Invalid Group ID")
        print(data)

    def tearDown(self):
        """
        Teardown method to clean up after each test.
        """
        self.storage.close()


if __name__ == '__main__':
    unittest.main()
