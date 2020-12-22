target = 10000
total_steps, \
    steps_difference = 0, 0
is_going_home = False
while total_steps < target:
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        total_steps += steps_to_home
        is_going_home = True
        break
    current_steps = int(command)
    total_steps += current_steps
if total_steps >= 10000:
    steps_difference = total_steps - target
    print(f"Goal reached! Good job!\n"
          f"{steps_difference} steps over the goal!")
else:
    steps_difference = target - total_steps
    print(f"{steps_difference} more steps to reach goal.")
