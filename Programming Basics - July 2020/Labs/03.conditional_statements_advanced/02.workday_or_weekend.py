day = input()
week_period = ''
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    week_period = 'Working day'
elif day == "Saturday" or day == 'Sunday':
    week_period = 'Weekend'
else:
    week_period = 'Error'
print(week_period)
