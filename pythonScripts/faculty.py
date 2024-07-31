from Schoolbase import SchoolBase as SB

class Faculty(SB):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.departments = []
        self.members = []
        

    def getDepartments(self):
        return self.departments
    def getMembers(self):
        return self.members
    
    def __str__(self) -> str:
        return super().__str__()
    
    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "departments": [department.to_dict() for department in self.departments],
            "members": [members.to_dict() for members in self.members]

        }
    
    