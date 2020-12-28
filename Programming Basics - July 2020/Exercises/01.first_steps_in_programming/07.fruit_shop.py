strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberries_price * 0.50
oranges_price = raspberries_price * 0.60
bananas_price = raspberries_price * 0.20

needed_money = (strawberries_price * strawberries_quantity)\
               + (raspberries_price * raspberries_quantity) +\
               (oranges_price * oranges_quantity) + \
               (bananas_price * bananas_quantity)
print(needed_money)
