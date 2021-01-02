fires_info = input().split("#")
water = int(input())
effort = 0

put_out_cells = []

for fire in fires_info:
    # split separated fires info
    tokens = fire.split(" = ")
    fire_type = tokens[0]
    value = int(tokens[1])
    # check fires category & value. Put it fire cell out if water is enough
    # calculating effort = 0.25 * fire value
    if water >= value:

        if (fire_type == "Low") and (1 <= value <= 50):
            water -= value
            put_out_cells.append(value)
            effort += value * 0.25

        elif (fire_type == "Medium") and (51 <= value <= 80):
            water -= value
            put_out_cells.append(value)
            effort += value * 0.25

        elif (fire_type == "High") and (81 <= value <= 125):
            water -= value
            put_out_cells.append(value)
            effort += value * 0.25

total_fire = 0
# print output
print("Cells:")
for cell in put_out_cells:
    total_fire += cell
    print(f" - {cell}")
print(f"Effort: {round(effort, 2)}")
print(f"Total Fire: {total_fire}")
