player = {}

player['a'] = list(input())
player['b'] = list(input())
player['c'] = list(input())
flag = 1
next_player = player['a'][0]
player['a'].pop(0)
while flag:
    if player[next_player]:
        before_player = next_player
        next_player = player[next_player][0]
        player[before_player].pop(0)
    else:
        break
print(next_player.upper())
