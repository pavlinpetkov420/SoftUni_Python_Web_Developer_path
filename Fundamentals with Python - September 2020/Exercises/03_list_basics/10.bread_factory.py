def rest_a_bit(energy, quantity):
    # if rest_energy_value + current one > 100 than fulfill to 100 from the rest_value energy else sum the values
    gained_energy, max_energy = 0, 100
    if energy + quantity > 100:
        gained_energy = max_energy - energy
        energy = max_energy
    else:
        energy += quantity
        gained_energy = quantity

    print(f"You gained {gained_energy} energy.\n"
          f"Current energy: {energy}.")
    return energy


def make_an_order(energy, coins, quantity):
    if energy - 30 < 0:
        print("You had to rest!")
        energy += 50
        return coins, energy
    else:
        energy -= 30
        coins += quantity
        print(f"You earned {quantity} coins.")
    return energy, coins


def buy_the_needed(coins, product, price):
    if coins - price <= 0:
        print(f"Closed! Cannot afford {product}.")
        return coins, True
    else:
        coins -= price
        print(f"You bought {product}.")
        return coins, False


def take_n_process_events():
    workday_events = input().split('|')
    energy, coins = 100, 100
    is_bankrupt = False
    for event in workday_events:
        if is_bankrupt:
            break
        action, quantity = event.split('-')
        quantity = int(quantity)
        if action == 'rest':
            # rest and collect some energy
            energy = rest_a_bit(energy, quantity)
        elif action == 'order':
            # make an order if it is possible
            energy, coins = make_an_order(energy, coins, quantity)
        else:
            # buying some stuff
            coins, is_bankrupt = buy_the_needed(coins, action, quantity)
    if not is_bankrupt:
        print("Day completed!\n"
              f"Coins: {coins}\n"
              f"Energy: {energy}")


take_n_process_events()
