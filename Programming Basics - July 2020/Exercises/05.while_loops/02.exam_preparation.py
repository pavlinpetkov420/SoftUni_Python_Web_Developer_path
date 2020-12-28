bad_grades_limit = int(input())
bad_grades_counter, \
    total_tasks, \
    grade_sum = 0, 0, 0
is_too_much_bad_grades = False
command = input()
while command != "Enough":
    task_name = command
    task_grade = int(input())
    if task_grade <= 4.00:
        bad_grades_counter += 1
    if bad_grades_limit <= bad_grades_counter:
        is_too_much_bad_grades = True
        break
    grade_sum += task_grade
    total_tasks += 1
    command = input()
if is_too_much_bad_grades:
    print(f"You need a break, {bad_grades_counter} poor grades.")
else:
    average_score = grade_sum / total_tasks
    print(f"Average score: {average_score:.2f}\n"
          f"Number of problems: {total_tasks}\n"
          f"Last problem: {task_name}")
