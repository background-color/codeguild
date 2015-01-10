__author__ = 'root'

ranks = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
deck = {}
card = 0
color = 'black'
for i in suits:
    if i == 'spades' or i == 'clubs':
        color = 'black'
    else:
        color = 'red'
    for j in ranks:
        card += 1
        d = {card: {"suit": i,
                    "rank": j,
                    "color": color}}
        deck.update(d)
for cards in deck:
    print(deck[cards])





# print deck





