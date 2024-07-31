from SchBaseAssgn import SchoolBase as ScB

class Faculty(ScB):
    def __init__(self, name, email, dean):
        super().__init__(name, email)
        self.departments = []
        self.dean = dean
        self.members = []


    def getDepartment(self):
        return self.departments
    def getDean(self):
        return self.dean
    
    def getMembers(self):
        return self.members
    
    def __str__(self):
        return super().__str__()
    
    def to_dict(self):
        return {
            "name" : self.name,
            "email": self.email,
            "departments": [departments.to_dict() for departments in self.departments],
            "dean": self.dean,
            "members": [members.to_dict() for members in self.members]
        }


