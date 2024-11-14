from user_data.base import DataSaver
from user_data.generators import UserDataGenerator


class UserDataService:
    def __init__(self, generator: UserDataGenerator, saver: DataSaver):
        self.generator = generator
        self.saver = saver

    def generate_and_save_users(self, num_users=100):
        users = [self.generator.generate_user_data() for _ in range(num_users)]
        self.saver.save(users)
