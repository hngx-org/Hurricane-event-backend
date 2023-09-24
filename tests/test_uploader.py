import unittest
from unittest.mock import patch
import uuid
from io import BytesIO
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
        self.storage = DBStorage()
        self.storage.load()

    def test_upload_image_success(self):
        """ 
        Succesfully uploads an image
        """
        with patch("cloudinary.uploader.upload") as mock_upload:
            mock_upload.return_value = {"secure_url": "https://example.com/image.jpg"}
            response = self.client.post(
                "/api/image-upload",
                content_type="multipart/form-data",
                data={"image": (BytesIO(b"fake_image_data"), "test.jpg")},
            )

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["message"], "success")
        self.assertEqual(data["url"], "https://example.com/image.jpg")
        print(data)

    def test_upload_image_failure(self):
        """ 
        Fails to upload an image with no image in request
        """
        response = self.client.post("/api/image-upload")
        
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data["message"], "No image in request")

    def test_upload_image_failure2(self):
        """ 
        Fails to upload an image with no image selected
        """
        response = self.client.post(
            "/api/image-upload",
            content_type="multipart/form-data",
            data={"image": (BytesIO(b""), "")},
        )
        
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data["message"], "No image selected")

    def tearDown(self):
        """
        Teardown method to clean up after each test.
        """
        self.storage.close()


if __name__ == '__main__':
    unittest.main()
