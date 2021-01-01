input_counter = int(input())
capacity = 0
for index in range(input_counter):
    liters = int(input())
    capacity += liters
    if capacity > 255:
        print("Insufficient capacity!")
        capacity -= liters
print(capacity)
