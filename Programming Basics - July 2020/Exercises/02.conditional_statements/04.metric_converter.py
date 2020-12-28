number = float(input())
input_unit = input()
output_unit = input()

if input_unit == 'mm':
    if output_unit == 'cm':
        number /= 10
    elif output_unit == 'm':
        number /= 1000
elif input_unit == 'cm':
    if output_unit == 'mm':
        number *= 10
    elif output_unit == 'm':
        number /= 100
elif input_unit == 'm':
    if output_unit == 'mm':
        number *= 1000
    elif output_unit == 'cm':
        number *= 100

print(f'{number:.3f}')
