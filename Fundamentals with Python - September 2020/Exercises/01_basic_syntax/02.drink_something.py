age = int(input())
output = None
if age <= 14:
    output = "drink toddy"
elif 15 <= age <= 18:
    output = "drink coke"
elif 19 <= age <= 21:
    output = "drink beer"
elif age > 21:
    output = "drink whisky"
print(output)
