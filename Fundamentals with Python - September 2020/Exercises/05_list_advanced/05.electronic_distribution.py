electrons_quantity = int(input())

electrons = []
shell_count = 1
while electrons_quantity > 0:
    shell = 2 * shell_count ** 2
    if shell > electrons_quantity:
        electrons.append(electrons_quantity)
    else:
        electrons.append(shell)
    electrons_quantity -= shell
    shell_count += 1

print(electrons)
