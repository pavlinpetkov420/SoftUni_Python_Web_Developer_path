from math import pi
figure_type = input()
area = 0
if figure_type == "square":
    side = float(input())
    area = side ** 2
elif figure_type == "rectangle":
    side = float(input())
    second_side = float(input())
    area = side * second_side
elif figure_type == "circle":
    radius = float(input())
    area = pi * (radius ** 2)
else:
    side_length = float(input())
    height_length = float(input())
    area = (side_length * height_length) / 2
print(f"{area:.3f}")