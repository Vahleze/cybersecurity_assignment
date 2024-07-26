from user import User

class Student(User):
    def __init__(self, firstname, lastname, email, password, regNo, department):
        super().__init__(firstname, lastname, email, password)
        self.regNo = regNo
        self.department = department

    def getregNo(self):
        return self.regNo
    
    def getStudentDetails(self):
        return f" firtsname: {self.firstname}\n lastname: {self.lastname}\nemail: {self.email} \npassword: {self.password} \nregNo: {self.regNo}\n department: {self.department}"