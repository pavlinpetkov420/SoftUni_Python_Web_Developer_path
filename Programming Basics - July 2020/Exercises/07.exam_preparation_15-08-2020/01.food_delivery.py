chicken_menu_amount = int(input())
fish_menu_amount = int(input())
vegetarian_menu_amount = int(input())
# # menus cost
# total_cost = (chicken_menu_amount * 10.35) + (fish_menu_amount * 12.40) + (vegetarian_menu_amount * 8.15)
# # add dessert price and delivery price
# total_cost += (total_cost * 0.20) + 2.50
# print(f"Total: {total_cost:.2f}")

chicken_menu = chicken_menu_amount * 10.35
fish_menu = fish_menu_amount * 12.40
veggie_menu = vegetarian_menu_amount * 8.15
total_cost = chicken_menu + fish_menu + veggie_menu
total_cost += (total_cost * 0.20) + 2.50
print(f"Total: {total_cost:.2f}")

"""Both problem solutions are with same time limit - 0.071"""
