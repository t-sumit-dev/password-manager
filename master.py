from pathlib import Path
from getpass import getpass
import hashlib
import json
class MasterAuth:
    def __init__(self):
        self.file = Path("master.json")

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def master_exists(self):
        return self.file.exists()

    def create_master_password(self):
        while True:
            password = getpass("Create Master Password: ")
            confirm = getpass("Confirm Master Password: ")

            if password != confirm:
                print("Passwords do not match. Try again.\n")
                continue

            if len(password) < 8:
                print("Master password must be at least 8 characters.\n")
                continue

            data = {
                "master_password": self.hash_password(password)
            }

            with open(self.file, "w") as file:
                json.dump(data, file, indent=4)

            print("Master password created successfully.\n")
            return

    def verify_master_password(self):
        with open(self.file, "r") as file:
            data = json.load(file)

        stored_hash = data["master_password"]

        for attempt in range(3):
            password = getpass("Enter Master Password: ")

            if self.hash_password(password) == stored_hash:
                print("Access granted.\n")
                return True

            print(f"Wrong password. {2 - attempt} attempts left.\n")

        print("Too many failed attempts. Exiting.")
        return False