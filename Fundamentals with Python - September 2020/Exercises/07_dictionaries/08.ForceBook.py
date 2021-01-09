class ForceBook:

    def __init__(self, force_side, force_user):
        self.force_side = force_side
        self.force_user = force_user
        self.my_force_book = {}

    def register(self, force_side='', force_user=''):
        if force_user not in self.my_force_book.items():
            self.my_force_book[force_side] = [force_user]
        else:
            self.my_force_book[force_side].append(self.force_user)

    def change_sides(self, force_user, force_side):
        is_found = False
        for side_one, user_one in self.my_force_book.items():
            if user_one == force_user:
                is_found = True
                taken_side = side_one
                self.my_force_book[taken_side].pop(user_one)
                self.my_force_book[force_side].append(force_user)
        if not is_found:
            ForceBook.register(force_side, force_user)
            print(f"{force_user} joins the {force_side} side!")

    def __repr__(self):
        output_data = ''
        sorted_sides_n_users = dict(sorted(self.my_force_book.items(), key=lambda x: (-len(x[1]), x[0])))
        for key, values in sorted_sides_n_users.items():
            if len(values) > 0:
                members_count = len(sorted_sides_n_users[key])
                output_data += f"Side: {key}, Members: {members_count}\n"
                for side_user in values:
                    output_data += f"! {side_user}\n"
        return output_data


force_book_object = ForceBook("", [])

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    delimiter_one = " | "
    delimiter_two = " -> "
    tokens = command.split(delimiter_one or delimiter_two)
    if delimiter_one:
        side, user = tokens[0], tokens[1]
        force_book_object.register(side, user)
    else:
        side, user = tokens[1], tokens[0]
        force_book_object.change_sides(user, side)

print(force_book_object)
