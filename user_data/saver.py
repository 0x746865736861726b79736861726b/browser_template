import os
import csv

from user_data.base import DataSaver


class CSVSaver(DataSaver):
    def __init__(self, filename="csv/users.csv"):
        self.filename = filename

    def save(self, data):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

        with open(self.filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "name",
                    "password",
                ],
            )
            if file.tell() == 0:
                writer.writeheader()

            for user in data:
                writer.writerow(user)
