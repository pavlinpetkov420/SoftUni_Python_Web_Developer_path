favourite_book = input()
command = input()
books_checked = 0
is_found = False
while command != "No More Books":
    current_book = command
    if favourite_book == current_book:
        print(f"You checked {books_checked} books and found it.")
        is_found = True
        break
    books_checked += 1
    command = input()
if not is_found:
    print(f"The book you search is not here!\n"
          f"You checked {books_checked} books.")
