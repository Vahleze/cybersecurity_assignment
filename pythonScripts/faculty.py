
class Faculty:
    def __init__(self, name, Id):
        self.name = name
        self.Id = Id

    def __str__(self):
        return f"{self.name} {self.Id}"
    
    def getName(self):
        return f"Welcome  to the {self.name}"
    
    def getFacultyDetails(self):
        return f"{self.name} {self.Id}"