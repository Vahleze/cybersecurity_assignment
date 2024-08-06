from user import User

class Lecturer(User):
    def __init__(self, firstname, lastname, email, password, staffId):
        super().__init__(firstname, lastname, email, password)
        self.staffId = staffId
        
    def getStaffId(self):
        return self.staffId
    
    def getLecturerDetails(self):
        return f" firstname: {self.firstname}\n lastname: {self.lastname}\nemail: {self.email}\n password: {self.password}\n staffId: {self.staffId}"
        

    def to_dict(self):
        return {
            "id" : self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "staffId": self.staffId
        }