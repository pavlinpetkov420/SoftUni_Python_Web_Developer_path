"""Do it without functions!!! Later!!! :)"""


def main_data_processing():
    special_materials = {"shards": 0, "motes": 0, "fragments": 0}
    junk_materials = {}
    is_more_materials_needed = True
    item = ""
    while is_more_materials_needed:
        materials_input = input().split()
        for index in range(0, len(materials_input), 2):
            name = materials_input[index + 1].lower()
            quantity = int(materials_input[index])
            if name == "shards":
                special_materials[name] += quantity
            elif name == "motes":
                special_materials[name] += quantity
            elif name == "fragments":
                special_materials[name] += quantity
            else:
                if name is junk_materials.keys():
                    junk_materials[name] += quantity
                else:
                    junk_materials[name] = quantity
            if special_materials["shards"] >= 250:
                item = "Shadowmourne"
                special_materials["shards"] -= 250
                is_more_materials_needed = False
                break
            elif special_materials["motes"] >= 250:
                item = "Dragonwrath"
                special_materials["motes"] -= 250
                is_more_materials_needed = False
                break
            elif special_materials["fragments"] >= 250:
                item = "Valanyr"
                special_materials["fragments"] -= 250
                is_more_materials_needed = False
                break
    return special_materials, junk_materials, item


def print_materials(materials_left, junk_materials):
    sorted_dictionary = dict(sorted(materials_left.items(), key=lambda x: (-x[1], x[0])))
    for name, quantity in sorted_dictionary.items():
        print(f"{name}: {quantity}")
    junk_materials = dict(sorted(junk_materials.items(), key=lambda x: x[0]))
    for name, quantity in junk_materials.items():
        print(f"{name}: {quantity}")


materials, junk, legendary_item = main_data_processing()
print(f"{legendary_item} obtained!")
print_materials(materials, junk)

special_materials = {"shards": 0, "motes": 0, "fragments": 0}
junk_materials = {}
is_more_materials_needed = True
item = ""
while is_more_materials_needed:
    materials_input = input().split()
    for index in range(0, len(materials_input), 2):
        name = materials_input[index + 1].lower()
        quantity = int(materials_input[index])
        if name == "shards":
            special_materials[name] += quantity
        elif name == "motes":
            special_materials[name] += quantity
        elif name == "fragments":
            special_materials[name] += quantity
        else:
            if name is junk_materials.keys():
                junk_materials[name] += quantity
            else:
                junk_materials[name] = quantity
        if special_materials["shards"] >= 250:
            item = "Shadowmourne"
            special_materials["shards"] -= 250
            is_more_materials_needed = False
            break
        elif special_materials["motes"] >= 250:
            item = "Dragonwrath"
            special_materials["motes"] -= 250
            is_more_materials_needed = False
            break
        elif special_materials["fragments"] >= 250:
            item = "Valanyr"
            special_materials["fragments"] -= 250
            is_more_materials_needed = False
            break

print(f"{item} obtained!")
sorted_dictionary = dict(sorted(special_materials.items(), key=lambda x: (-x[1], x[0])))
for name, quantity in sorted_dictionary.items():
    print(f"{name}: {quantity}")
junk_materials = dict(sorted(junk_materials.items(), key=lambda x: x[0]))
for name, quantity in junk_materials.items():
    print(f"{name}: {quantity}")



