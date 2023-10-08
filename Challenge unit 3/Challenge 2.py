class Student:
  
  def __init__(self, name, roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa
    
    
def sort_students(student_list):

 sorted_students=sorted(student_list, 
  key=lambda student:student.cgpa, reverse=True)
 return sorted_students


students = [
  Student("Aan", "A123", 7.3),
  Student("jasmine", "A124", 5.9),
  Student("arsha", "A125", 6.9),
  Student("priyanka", "A126", 4.9),
]

sorted_students = sort_students(students)


for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))
  
  