import math
world_record = float(input())
distance_in_meters = float(input())
time_for_meter = float(input())
swimmer_time = distance_in_meters * time_for_meter
time_delay = math.floor((distance_in_meters / 15)) * 12.5
swimmer_time += time_delay
if world_record > swimmer_time:
    print(f'Yes, he succeeded! The new world record is {swimmer_time:.2f} seconds.')
else:
    time_needed = abs(world_record - swimmer_time)
    print(f'No, he failed! He was {time_needed:.2f} seconds slower.')
