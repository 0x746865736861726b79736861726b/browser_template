import csv

from user_data.base import DataSaver


class CSVSaver(DataSaver):
    def __init__(self, filename="users.csv"):
        self.filename = filename

    def save(self, data):
        with open(self.filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "name",
                    "last_name",
                    "email",
                    "password",
                ],
            )
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)
