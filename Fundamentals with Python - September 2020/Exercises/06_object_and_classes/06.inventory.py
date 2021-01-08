class Inventory:
    items = []

    def __init__(self, capacity=int):
        self.__capacity = capacity

    def __repr__(self):

        capacity_left = self.__capacity - len(self.items)
        output = f"Items: {', '.join(Inventory.items)}.\n" \
                 f"Capacity left: {capacity_left}"

    def add_item(self, item):
        if self.__capacity > len(Inventory.items):
            Inventory.items.append(item)
        else:
            return print('not enough room in the inventory')

    def get_capacity(self):
        return self.__capacity


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
