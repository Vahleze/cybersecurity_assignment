from faculty import Faculty
import datetime

class Department(Faculty):
    def __init__(self, name, Id, Name, departmentId):
         super().__init__(name, Id)
         self.Name = Name
         self.departmentId = departmentId
         self.created_at = datetime.datetime.now()


    def __str__(self):
         return f"{self.Name} {self.departmentId}"
    
    def getName(self):
         return f"This is {self.Name}"
    
    def getDepartmentId(self):
         return self.departmentId
    
    def getDepartmentDetails(self):
         return f"The department details are:\nFaculty: {self.name}\nId: {self.Id}\nDeparment: {self.Name}\nDepartmentID: {self.departmentId}\ncreatedAt: {self.created_at}"
         
    
