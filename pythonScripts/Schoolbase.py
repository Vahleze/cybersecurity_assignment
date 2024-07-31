import datetime
import uuid

class SchoolBase:
    def __init__(self, name, email):
        self.Id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.createdAt = datetime.datetime.now()

    def getId(self):
        return self.Id 
    def getName(self):
        return self.name
    