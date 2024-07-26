from student import Student
from lecturer import Lecturer

student1 = Student("Emeka", "Eze", "emeka@gmail.com", "emeka121", "LISTAC/101/55", "Cybersecurity")
student2 = Student("Mike", "Okoro", "okoromike90@gmail.com", "okokomiko1357", "LISTAC/111/622", "Machine_Learning")

lecturer1 = Lecturer("Miracle", "Sixtus", "mimigenuis042@gmail.com", "mimi007", "LIS720")
lecturer2 = Lecturer ("Cletus", "Ohamadike", "ohamadike1@gmail.com", "ohamadikennobi2020", "LIS200")



print(student1.getLoginDetails())
print(student1.getStudentDetails())

print(student2.getLoginDetails())
print(student2.getStudentDetails())

print(lecturer1.getLoginDetails())
print(lecturer1.getLecturerDetails())

print(lecturer2.getLoginDetails())
print(lecturer2.getLecturerDetails())