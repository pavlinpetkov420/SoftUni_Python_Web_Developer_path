length = int(input())
width = int(input())
height = int(input())
occupied_volume_percent = float(input())

aquarium_volume = length * width * height
volume_in_liters = aquarium_volume * 0.001
free_volume = volume_in_liters * (1 - (occupied_volume_percent * 0.01))

print(free_volume)
