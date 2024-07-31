from faculty_Assgn29_07_24 import Faculty as fac
from departmentAssgn29_07_24 import department as dep
from course_Assg29_07_24 import Course as cou
import json

faculty1 = fac("Physical and Applied Science", "FOPAS@gmail.com", "Prof. Mattew Obafemi")
faculty2 = fac("Medical Science", "FOMS@gmail.com", "Prof. Dr. Chimbuchi Obioma")
department1 = dep("Computer Scicence", "csc@gmail.com", faculty1.id, "Prof. Ken Brown")
print(faculty1)
faculty1.departments.append(department1)
print(department1)
print(faculty1.departments)
print(faculty2)
department2 = dep("Mathematics", "maths@gmail.com", faculty1.id, "Prof. Olusegun Oloun")
faculty1.departments.append(department2)
department3 = dep("Medicine and Surgery", "medsurg@gmail.com", faculty2.id, "Dr. Nicolas Ego")
department4 = dep("Nursing", "nursing@gmail.com", faculty2.id, "Madam Nkechi Nwogu(Ns. MSc. Nrr)")
faculty2.departments.append(department3)
faculty2.departments.append(department4)
course1 = cou("Introduction to Computers", "CSC101", department1.id)
course2 = cou("History of Computers", "CSC112", department1.id)
course3 = cou("Elementary Mathematics", "MTH111", department2.id)
course4 = cou("Algebraic Expression", "MTH121", department2.id)
course5 = cou("GeneralnBiology", "BIO111", department3.id)
course6 = cou("Anatomy", "BIO131", department3.id)
course7 = cou("Introduction to Nursing Practices", "NUR111", department4.id)
course8 = cou("Anatomy II", "BIO141", department4.id)


fac = open("myFiles/faculty.json", "w")
fac.write(json.dumps(faculty1.to_dict(), indent=4, separators=(", " , " : "), sort_keys=True))
fac = open("myFiles/faculty.json", "a") 
fac.write(json.dumps(faculty2.to_dict(), indent=4, separators=(", " , " : "), sort_keys=True))
fac.close()
dept = open("myFiles/department.json", "w")
departmentList = [department1.to_dict(), department2.to_dict(), department3.to_dict(), department4.to_dict()]
dept.write(json.dumps(departmentList, indent=4, separators=(" , " , " : " ), sort_keys=True))
dept.close()
cour = open("myFiles/course.json", "w")
courseList = [course1.to_dict(), course2.to_dict(), course3.to_dict(), course4.to_dict(), course5.to_dict(), course6.to_dict(), course7.to_dict(), course8.to_dict()]
cour.write(json.dumps(courseList, indent=4, separators= (" , " , " : "), sort_keys=True))
cour.close()