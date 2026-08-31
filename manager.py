from credential import Credential
from datetime import datetime
import secrets
import string
import random
import hashlib
import json
class Passsword_manager:
    def __init__(self):
        self.credentail = []
        self.load_from_file()
    def save_to_file(self):
        details = [data.to_dict() for data in self.credentail]
        with open("password.json","w") as file:
            json.dump(details,file,indent = 4)
    def load_from_file(self):
        try:
            with open("password.json", "r") as file:
                details = json.load(file)
            for data in details:
                data_obj = Credential.from_dict(data)
                self.credentail.append(data_obj)
        except (FileNotFoundError,json.JSONDecodeError):
            pass
    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()
    def verify_password(self,password,stored_hash):
        return self.hash_password(password) == stored_hash
    def generate_password(self,length = 16):
        if length < 4:
            raise ValueError("Password length must be at least 4.")
        password = [secrets.choice(string.ascii_uppercase),
                    secrets.choice(string.ascii_lowercase),
                    secrets.choice(string.digits),
                    secrets.choice(string.punctuation)
                    ]
        all_character = (string.ascii_letters + string.digits + string.punctuation)
        for i in range(length - 4):
            password.append(secrets.choice(all_character))
        random.shuffle(password)
        return "".join(password)
    def add_credential(self,data):
        for existing_email in self.credentail:
            if existing_email.email == data.email:
                print("Email already exists.\n")
                return
        data.password = self.hash_password(data.password)
        self.credentail.append(data)
        print("\n Data added successfuly.\n")
        self.save_to_file()
    def view_credential(self):
        if not self.credentail:
            print("No data found.\n")
            return
        for data in self.credentail:
            data.display()
    def delete_credential(self,email):
        for data in self.credentail:
            if data.email == email:
                while True:
                    password = input("Enter your password : ")
                    if self.verify_password(password,data.password):
                        self.credentail.remove(data)
                        print("Data deleted successfully.\n")
                        self.save_to_file()
                        break
                    else:
                        print("Wrong password\n")
        print("Data not found.\n")
    def search_by_website(self,website):
        for data in self.credentail:
            if data.website == website:
                data.display()
                return
        print("Data not found.\n")
    def update_credential(self,website):
        for data in self.credentail:
            if data.website == website:
                while True:
                    password = input("Enter your password : ")
                    if self.verify_password(password, data.password):
                        data.email = input("Enter new email : ")
                        data.username = input("Enter new username : ")
                        new_password = input("Enter new password : ")
                        data.password = self.hash_password(new_password)
                        data.created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print("\n Data updated successfuly.\n")
                        self.save_to_file()
                        return
                    else:
                        print("Wrong password\n")
        print("Data not found.\n")
    