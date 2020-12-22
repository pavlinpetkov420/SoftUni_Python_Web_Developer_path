sum_prime_numbers, \
    sum_non_prime_numbers = 0, 0

command = input()
while command != "stop":
    is_prime = True
    number = int(command)
    if number == 1:
        is_prime = False
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    else:
        for d in range(2, number):
            if number % d == 0:
                is_prime = False
        if is_prime:
            sum_prime_numbers += number
        else:
            sum_non_prime_numbers += number
    command = input()

print("Sum of all prime numbers is: " + str(sum_prime_numbers))
print("Sum of all non prime numbers is: " + str(sum_non_prime_numbers))
