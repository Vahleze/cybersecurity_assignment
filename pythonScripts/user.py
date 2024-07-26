import datetime


class User:
    def __init__(self, firtsname, lastname, email, password):
        self.firstname = firtsname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.created_at = datetime.datetime.now()


    def __str__(self):
        return f"{self.firstname} with the Email; {self.email}"
    
    def greet(self):
        return f"Hello, my name is {self.firstname} {self.lastname}"    
    
    def getLoginDetails(self):
        return f"Email: {self.email} \n Password: {self.password}"