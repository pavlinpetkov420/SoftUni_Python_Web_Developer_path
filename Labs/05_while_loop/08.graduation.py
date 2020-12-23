student_name = input()
grades_sum, \
    grade_counter, \
    fail_counter = 0, 0, 0
is_excluded = False
while grade_counter < 12:
    grade = float(input())
    if grade < 4.00:
        fail_counter += 1
        if fail_counter > 1:
            is_excluded = True
            print(student_name + " has been excluded at "
                  + str(grade_counter) + " grade")
            break
    grades_sum += grade
    grade_counter += 1
average_grade = grades_sum / grade_counter
if not is_excluded:
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
