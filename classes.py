import random

class Card:
    def __init__(self, suit, rank, id):
        CARDRANK = [x for x in str('23456789TJQK')]
        CARDSUIT = ['h','d','s','c']

        self.rank = rank
        self.suit = suit
        self.id = id
        self.name = f'{CARDRANK[rank]}{CARDSUIT[suit]}'

    def __repr__(self):
         return self.name

    def __iter__(self):
        return self

    def __lt__(self, other):
        if isinstance(other, Card):
           return self.id < other.id
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Card):
            return self.rank + other.rank

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank
        else:
            return False

class Deck:
    def __init__(self):
        self.deck = []
        num = 0
        for suit in range(4):
            for rank in range(12):
                card = Card(suit, rank, num)
                self.deck.append(card)
                num += 1

    def __getitem__(self,s):
        return self.deck[s]

    def __iter__(self):
        return self

class Race:
    def __init__(self):
        self.parcours = []
        playdeck = Deck()
        self.stock = playdeck[:]
        random.shuffle(self.stock)
        for _ in range(7):
            card = self.stock.pop()
            self.parcours.append(card)

class Horse:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.races_won = 0

    def __repr__(self):
        return self.name
        

class Punter:
    def __init__(self):
        self.name = 'Punter'
        self.bankroll = 100


