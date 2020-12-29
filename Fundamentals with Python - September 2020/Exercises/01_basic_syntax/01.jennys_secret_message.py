name = input()
output = ''
if name == "Johnny":
    output = "Hello, my love!"
else:
    output = "Hello, {}!".format(name)
print(output)
