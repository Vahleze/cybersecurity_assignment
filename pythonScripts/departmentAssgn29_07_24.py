from SchBaseAssgn import SchoolBase as ScB

class department(ScB):
    def __init__(self, name, email, facultyId, HOD):
        super().__init__(name, email)
        self.facultyId = facultyId
        self.HOD = HOD
        self.lecturers = []
        self.courses = []

    def getHOD(self):
         return self.HOD

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
            "Id": self.id,
            "name": self.name,
            "email": self.email,
            "facultyId": self.facultyId,
            "HOD": self.HOD,
            "lecturers": [lecturer.to_dict() for lecturer in self.lecturers],
            "courses": [course.to_dict() for course in self.courses]
        }