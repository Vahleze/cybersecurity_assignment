import datetime
import uuid

class SchoolBase:
    def __init__(self, name, email):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.createdAt = datetime.datetime.now()


    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.name