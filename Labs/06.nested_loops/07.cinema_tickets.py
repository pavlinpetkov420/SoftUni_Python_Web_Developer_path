total_tickets = 0
student_counter = 0
kids_counter = 0
standard_counter = 0
current_movie_counter = 0
is_finished = False

while True:
    input_data = input()
    movie_name = input_data
    hall_capacity = int(input())
    while True:
        input_data = input()
        if (input_data == "End") or (hall_capacity == current_movie_counter) or (input_data == "Finish"):
            if input_data == "Finish":
                is_finished = True
            occupancy_percentage = current_movie_counter / hall_capacity * 100
            print(f"{movie_name} - {occupancy_percentage:.2f}% full.")
            break

        ticket_type = input_data
        if ticket_type == "standard":
            standard_counter += 1
        elif ticket_type == "student":
            student_counter += 1
        elif ticket_type == "kid":
            kids_counter += 1
        current_movie_counter += 1

    total_tickets += current_movie_counter
    if is_finished or (hall_capacity == current_movie_counter):
        break
    current_movie_counter = 0

student_percentage = student_counter / total_tickets * 100
standard_percentage = standard_counter / total_tickets * 100
kid_percentage = kids_counter / total_tickets * 100
print(f"Total tickets: {total_tickets}\n"
      f"{student_percentage:.2f}% student tickets.\n"
      f"{standard_percentage:.2f}% standard tickets.\n"
      f"{kid_percentage:.2f}% kids tickets.")
