from Schoolbase import SchoolBase as SB

class Department(SB):
     def __init__(self, name, email, facultyId):
         super().__init__(name, email)
         self.facultyId = facultyId
         self.lecturers = []
         self.courses = []



     def getLecturers(self):
         return self.lecturers
    
     def getCourses(self):
          return self.courses
     
     def getId(self):
            return f"{self.name} {self.email}"
    


     def __str__(self):
         return super().__str__()+ " " + str(self.facultyId)
     

     def to_dict(self):
        return {
            "Id": self.Id,
            "name": self.name,
            "email": self.email,
            "facultyId": self.facultyId,
            "lecturers": [lecturer.to_dict() for lecturer in self.lecturers],
            "courses": [course.to_dict() for course in self.courses]
        }
    