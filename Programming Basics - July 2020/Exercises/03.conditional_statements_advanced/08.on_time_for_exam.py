exam_start_hour = int(input())
exam_start_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_start = (exam_start_hour * 60) + exam_start_minute
arrival = (arrival_hour * 60) + arrival_minute
difference = exam_start - arrival
state = ""
if 0 <= difference <= 30:
    state = "On time"
elif difference > 30:
    state = "Early"
elif difference < 0:
    state = "Late"
difference = abs(difference)
hours = difference // 60
minutes = difference % 60
if state == 'On time':
    if difference == 0:
        print(state)
    else:
        print(state)
        print(f"{difference} minutes before the start")
elif state == "Early":
    if 30 > difference or difference < 60:
        print(state)
        print(f"{difference} minutes before the start")
    else:
        print(state)
        print(f"{hours}:{minutes:02d} hours before the start")
elif state == "Late":
    if difference < 60:
        print(state)
        print(f"{difference} minutes after the start")
    else:
        print(state)
        print(f"{hours}:{minutes:02d} hours after the start")