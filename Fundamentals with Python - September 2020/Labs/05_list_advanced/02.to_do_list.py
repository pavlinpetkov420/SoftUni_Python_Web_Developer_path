# append 10 zero string for indices
to_do_list = ['0' for _ in range(10)]

# process the input to_do's and place them in their places
while True:
    command = input()
    if command == "End":
        break
    tokens = command.split('-')
    importance = int(tokens[0])
    task = tokens[1]

    to_do_list.insert(importance, task)

# assign tasks != 0 in result list
result = [task for task in to_do_list if not task == 0]
print(result)

# """v2.0"""
# # append ten None values for indices
# to_do_list = [None for _ in range(10)]
#
# # process the input to_do's and place them in their places
# while True:
#     command = input()
#     if command == "End":
#         break
#     tokens = command.split('-')
#     importance = int(tokens[0])
#     task = tokens[1]
#
#     to_do_list.insert(importance, task)
#
# # assign task in result list
# result = [task for task in to_do_list if task]
# print(result)
