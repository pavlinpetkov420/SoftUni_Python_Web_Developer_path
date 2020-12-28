import math
first_competitor = int(input())
second_competitor = int(input())
third_competitor = int(input())
total_time = first_competitor \
             + second_competitor\
             + third_competitor
minutes = total_time / 60
seconds = total_time % 60
minutes = math.floor(minutes)
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
