class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, new_product):
        Catalogue.products.append(new_product)

    def get_by_letter(self, letter):
        needed_products = [Catalogue.products[i]
                           for i in range(len(Catalogue.products))
                           if Catalogue.products[i][0] == letter]
        return needed_products

    def __repr__(self):
        Catalogue.products.sort()
        output = f"Items in the {self.name} catalogue:\n" + '\n'.join(Catalogue.products)
        return output


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
