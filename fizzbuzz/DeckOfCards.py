__author__ = 'root'

ranks = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
deck = {}
card = 0
color = 'black'
for suit in suits:
    if suit == 'spades' or suit == 'clubs':
        color = 'black'
    else:
        color = 'red'
    for rank in ranks:
        card += 1
        d = {card: {"suit": suit,
                    "rank": rank,
                    "color": color}}
        deck.update(d)

for card in deck:
    print deck[card]["rank"], deck[card]["suit"]





# print deck





