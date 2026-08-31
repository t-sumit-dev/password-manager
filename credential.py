from datetime import datetime
class Credential:
    def __init__(self,website,email,username,password,created_date = None):
        self.__website = website
        self.__email = email
        self.__username = username
        self.__password = password
        if created_date is None :
            self.__created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.__created_date = created_date
    #website
    @property
    def website(self):
        return self.__website

    @website.setter
    def website(self,value):
        if value.strip() == "":
            raise ValueError("Website cannot be empty.")
        self.__website = value

    #email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,value):
        if value.strip() == "":
            raise ValueError("Email cannot be empty.")
        self.__email = value

    #username
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self,value):
        if value.strip() == "":
            raise ValueError("Username cannot be empty.")
        self.__username = value

    #password
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,value):
        if value.strip() == "":
            raise ValueError("Password cannot be empty.")
        self.__password = value

    @property
    def created_date(self):
        return self.__created_date

    @created_date.setter
    def created_date(self,value):
        self.__created_date = value
    def display(self):
        print(F"WEBSITE : {self.website}")
        print(F"EMAIL : {self.email}")
        print(F"USERNAME : {self.username}")
        print(F"PASSWORD : {self.password}")
        print(F"CREATED DATE : {self.created_date}")
        print()
    def to_dict(self):
            return{
                "website" : self.website,
                "email" : self.email,
                "username" : self.username,
                "password" : self.password,
                "created_date" : self.created_date
            }
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["website"],
            data["email"],
            data["username"],
            data["password"],
            data["created_date"]
            )