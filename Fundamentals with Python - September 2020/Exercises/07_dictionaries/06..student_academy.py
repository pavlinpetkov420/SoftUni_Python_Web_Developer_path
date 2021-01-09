def process_data():
    input_counts = int(input())

    grades_dictionary = {}
    for n in range(0, input_counts):
        name = input()
        grade = float(input())

        if name not in grades_dictionary.keys():
            grades_dictionary[name] = []
        grades_dictionary[name].append(grade)

    return grades_dictionary


def calculate_average_grades(grades):
    filtered_grades = {}

    for name, grades_list in grades.items():

        total = 0
        for grade in grades_list:
            total += grade
        average = total / len(grades_list)

        if average >= 4.50:
            filtered_grades[name] = average

    return filtered_grades


def sort_n_print(names_n_average_grades):
    sorted_names_n_grades = dict(sorted(names_n_average_grades.items(), key=lambda x: x[0], reverse=True))
    for name, grade in sorted_names_n_grades.items():
        print(f"{name} -> {grade:.2f}")


# function for user input data and save it into a dictionary
students_n_grades = process_data()

# function for calculation of average grade on each student and record only those with 4.50 or higher
average_grades_filtered = calculate_average_grades(students_n_grades)

# sort grades descending and print them as is shown in the condition
sort_n_print(average_grades_filtered)
