import unittest
from faker import Faker
from src.user import User

class UserTests(unittest.TestCase):
    def setUp(self):
        self.faker = Faker(locale="es")

    def test_user_creation(self):
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(name=name_generated, email=email_generated)

        self.assertEqual(user.name, name_generated)
        self.assertEqual(user.email, email_generated)