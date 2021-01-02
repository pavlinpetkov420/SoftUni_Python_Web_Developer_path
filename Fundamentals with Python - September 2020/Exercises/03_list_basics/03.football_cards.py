red_cards = list(input().split())
team_a, \
    team_b = 11, 11
sent_off_players = []
is_over = False
for index in range(len(red_cards)):
    rc_team = red_cards[index][0]
    rc_number = red_cards[index][2]
    if red_cards[index] in sent_off_players:
        continue
    if rc_team == 'A':
        team_a -= 1
        sent_off_players.append(red_cards[index])
    else:
        team_b -= 1
        sent_off_players.append(red_cards[index])
    if (team_a < 7) or (team_b < 7):
        is_over = True
        break
output = ""
if is_over:
    output = f"Team A - {team_a}; Team B - {team_b}\n" \
             f"Game was terminated"
else:
    output = f"Team A - {team_a}; Team B - {team_b}"
print(output)
