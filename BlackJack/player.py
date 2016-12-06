from deck import Deck

class Player(object):
    """
    Player has private_card_list which store the cards, name
    """
    def __init__(self, playerName):
        self.private_card_list = []
        self.name = playerName
        self.points = 0

    def draw(self, deck):
        # Get the first card from the deck stack
        self.private_card_list.append(deck.cards[0])
        deck.removeTopCard()

    def calculate(self):
        # Figure out how many points
        points = 0
        numberOfAces = 0
        for card in self.private_card_list:
            temp = card.split()
            if temp[0].isdigit():
                points += int(temp[0])
            elif temp[0] == 'Ace':
                points += 11
                numberOfAces += 1
            else:
                points += 10

        while numberOfAces >0 and points > 21:
            numberOfAces -= 1
            points -= 10

        return points



