width = int(input())
length = int(input())
height = int(input())
apartment_volume = width * length * height
box_volume = 1 ** 3
command = input()
is_space_left = True
while command != "Done":
    box_count = int(command)
    current_boxes_volume = box_count * box_volume
    apartment_volume -= current_boxes_volume
    if apartment_volume <= 0:
        is_space_left = False
        print(f"No more free space! You need {abs(apartment_volume)} Cubic meters more.")
        break
    command = input()
if is_space_left:
    print(f"{apartment_volume} Cubic meters left.")
