import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Jenkins CI/CD Pipeline is working.",
            response.data
        )


if __name__ == "__main__":
    unittest.main()