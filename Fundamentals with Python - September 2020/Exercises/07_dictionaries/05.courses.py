def process_data():
    courses_n_students = {}

    while True:
        command = input()
        if command == "end":
            return courses_n_students
        course, student = command.split(" : ")
        if course not in courses_n_students.keys():
            courses_n_students[course] = []
        courses_n_students[course].append(student)


def print_data(courses_data):
    ordered_dictionary = dict(sorted(courses_data.items(), key=lambda x: len(x[1]), reverse=True))
    for course, names in ordered_dictionary.items():
        people_on_course = len(ordered_dictionary[course])
        print(f"{course}: {people_on_course}")
        for student in sorted(names):
            print(f"-- {student}")


courses = process_data()
print_data(courses)
