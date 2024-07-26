from department import Department
import datetime

class Course(Department):
    def __init__(self, name, Id, Name, departmentId, courseName, courseCode):
        super().__init__(name, Id, Name, departmentId)
        self.courseName = courseName
        self.courseCode = courseCode
        self.createdAt = datetime.datetime.now()

    def getCourseDetails(self):
        return f"Course details:\nFaculty: {self.name}\nFacultyID: {self.Id}\nDepartment: {self.Name}\nDepartmentID: {self.departmentId}\nCourse: {self.courseName}\nCourseCode: {self.courseCode}\nCreatedAt: {self.createdAt}"
    

