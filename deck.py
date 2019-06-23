import random
from collections import deque
from functools import total_ordering

class Card:
    value_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                  '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 1}
                  
    def __init__(self,number,suit):
        self.number = number
        self.suit = suit

    # Modify the __cmp__ for war game
    def __eq__(self,other):
        return (self.number == other.number)
    
    def __nq__(self,other):
        return (self.number != other.number)
    
    def __lt__(self,other):
        if self==other:
            return False
        if self.number=='A':
            return False
        elif other.number=='A':
            return True
        else:
            return self.value_dict[self.number]<self.value_dict[other.number]

    def __repr__(self):
        return ('{}{}'.format(self.number, self.suit))

class Deck:
    def __init__(self):
        self.cards = deque()
        self.initialize_deck()

    def initialize_deck(self):
        for num in Card.value_dict.keys():
            for suit in "cdhs":
                self.cards.append(Card(num,suit))

    def shuffle(self):
        random.shuffle(self.cards)    
    
    def draw_card(self):
        if not self.is_empty():
            card = self.cards.popleft()
            return card

    def add_cards(self,cards):
        self.cards.extend(cards)

    def is_empty(self):
        return not self.cards
    
    def deck_size(self):
        return len(self.cards)