class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def __repr__(self):
        output = f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"
        return output

    def add_student(self, student_name, grade):

        if Class.__students_count >= 1:
            self.students.append(student_name)
            self.grades.append(grade)

    def get_average_grade(self):
        sum_of_grades = 0
        for grade in self.grades:
            sum_of_grades += grade
        average_grade = sum_of_grades / len(self.grades)
        average_grade = f"{average_grade:.2f}"
        average_grade = float(average_grade)
        return average_grade




a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
