budget = float(input())
flour_price = float(input())
# calculated prices are for 1 pack of eggs and 0.250 L milk
# recipe - 1 pack eggs, 0.250 milk & 1 kg flour
eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) * 0.25
sweetbread_price = flour_price + eggs_price + milk_price
sweetbread_counter, \
    colored_eggs = 0, 0

while True:
    if budget < sweetbread_price:
        print("You made {} cozonacs! Now you have {} eggs and {:.2f}BGN left."
              .format(sweetbread_counter, colored_eggs, budget))
        break
    budget -= sweetbread_price
    sweetbread_counter += 1
    colored_eggs += 3
    if sweetbread_counter % 3 == 0:
        colored_eggs -= (sweetbread_counter - 2)
