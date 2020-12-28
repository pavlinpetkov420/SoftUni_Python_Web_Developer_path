book_pages = int(input())
pages_per_hour = int(input())
target_days = int(input())

total_time = book_pages / pages_per_hour
time_per_day = total_time / target_days

print(time_per_day)