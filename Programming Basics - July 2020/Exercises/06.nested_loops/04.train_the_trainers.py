judges_count = int(input())
command = input()
presentation_counter, \
    grade_sum = 0, 0
while command != "Finish":
    presentation_name = command
    current_presentation_average, \
        current_presentation_grade = 0, 0

    for judge in range(1, judges_count + 1):
        grade = float(input())
        current_presentation_grade += grade

    current_presentation_average = current_presentation_grade / judges_count
    grade_sum += current_presentation_average
    print(f"{presentation_name} - {current_presentation_average:.2f}.")
    current_presentation_average, \
        current_presentation_grade = 0, 0
    presentation_counter += 1
    command = input()

average_grade = grade_sum / presentation_counter
print(f"Student's final assessment is {average_grade:.2f}.")
