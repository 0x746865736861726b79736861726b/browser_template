import random
import string

from faker import Faker


fake = Faker()


class UserDataGenerator:
    def generate_first_name(self):
        return fake.name()

    def generate_last_name(self):
        return fake.last_name()

    def generate_email(self):
        return fake.email()

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        return password

    def generate_user_data(self):
        name = self.generate_first_name()
        last_name = self.generate_last_name()
        email = self.generate_email()
        password = self.generate_password()
        return {
            "name": name,
            "password": password,
        }
