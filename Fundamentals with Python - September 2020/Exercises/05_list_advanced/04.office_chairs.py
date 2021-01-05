rooms = int(input())
left = 0
enough_in_rooms = 0
for i in range(1, rooms + 1):
    room_presence = input().split()
    chairs = room_presence[0]
    free_chairs = int(room_presence[1])

    chairs_count = chairs.count('X')
    left_or_needed = chairs_count - free_chairs
    if left_or_needed >= 0:
        left += left_or_needed
        enough_in_rooms += 1
        continue
    else:
        print(f"{abs(left_or_needed)} more chairs needed in room {i}")

if enough_in_rooms == rooms:
    print(f"Game On, {left} free chairs left")
