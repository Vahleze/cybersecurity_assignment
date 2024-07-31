import uuid

        
class Course():
    def __init__(self, title, code, departmentId):
        self.id = str(uuid.uuid4())
        self.title = title
        self.code = code
        self.departmentId = departmentId



    def __str__(self) -> str:
        return f"{self.code} {self.title}"
    
    def getId(self):
        return self.id
    

    def to_dict(self):
        return {
            "id" : self.id,
            "title": self.title,
            "code": self.code,
            "departmentId": self.departmentId,

        }        
    
    