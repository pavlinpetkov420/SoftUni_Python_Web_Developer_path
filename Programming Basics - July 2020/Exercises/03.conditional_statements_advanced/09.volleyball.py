import math
leap_or_normal = input()
holidays = int(input())
hometown_weekends = int(input())
total_games = 0
total_weekends = 48 - hometown_weekends
total_games += hometown_weekends
total_games += total_weekends * 3/4
total_games += holidays * 2/3
if leap_or_normal == 'leap':
    total_games = math.floor(total_games * 1.15)
print(int(total_games))