def perfect_number_validator(num):
    half_num = num // 2
    divisors_sum = 0
    for n in range(1, half_num + 1):
        if num % n == 0:
            divisors_sum += n
    if divisors_sum == num:
        return True
    else:
        return False


number = int(input())
is_perfect = perfect_number_validator(number)
if is_perfect:
    print("We have a perfect number!")
elif not is_perfect:
    print("It's not so perfect.")
