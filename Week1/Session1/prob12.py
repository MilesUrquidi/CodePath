"""
Write a function shuffle() that accepts a list cards of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the list in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(cards):
	pass
Example Usage

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
shuffle(cards)

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
shuffle(cards)

cards = [10, 10, 2, 2]
shuffle(cards)
Example Output:

['Joker', 3, 'Queen', 'Ace', 2, 7]
[9, 'Joker', 2, 3, 3, 2, 'Joker', 9]
[10, 2, 10, 2]

U: split the cards in half, and them display them in alternating order
P: find the halfpoint of how many cards by dividing the length by 2,have the first half be x and second half be y, use slicing then have it alternate?
"""

def shuffle(cards):
    output = []
    mid = int(len(cards)/2)
    x = cards[:mid]
    y = cards[mid:]
    for i in range(mid):
        output.append(x[i])
        output.append(y[i])
    print(output)

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
shuffle(cards)

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
shuffle(cards)

cards = [10, 10, 2, 2]
shuffle(cards)