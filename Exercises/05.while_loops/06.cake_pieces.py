# define cake sizes
width = int(input())
length = int(input())
# calculate total pieces
total_pieces = width * length
pieces_counter = 0
# extra variable for case condition
is_cake_over = False
command = input()
while command != "STOP":
    pieces_taken = int(command)
    pieces_counter += pieces_taken

    if pieces_counter >= total_pieces:
        pieces_needed = int(pieces_counter - total_pieces)
        print(f"No more cake left! You need {pieces_needed} pieces more.")
        is_cake_over = True
        break
    command = input()

if not is_cake_over:
    pieces_left = int(total_pieces - pieces_counter)
    print(f"{pieces_left} pieces are left.")
