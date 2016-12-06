from deck import Deck
from player import Player

class Game(object):
    def __init__(self):
        self.player1 = Player('player1')
        self.player2 = Player('player2')
        self.dealer = Player('dealer')
        # Game order
        self.playerList = [self.player1, self.player2, self.dealer]
        self.terminal = False
        self.deck = Deck()
        self.deck.shuffle()
        # Every one get two cards sequentially
        for player in self.playerList:
            player.draw(self.deck)
            player.draw(self.deck)

        self.player1points= self.player1.calculate()
        self.player2points= self.player2.calculate()
        self.dealerpoints= self.dealer.calculate()

    def step(game, player1points, player2points, dealerpoints, action1, action2, reward1, reward2):
        """
        Return the next game state and reword, given current state and actions.
        :param state: including the player1point, player2point, dealerpoint
        :param action: 0 or 1, refer to hit or stick, respectively.
        : return a tuple (next game state, rewords)
        """

        if action1 == 0:
            game.player1.draw(game.deck)
            player1points = game.player1.calculate()
            # if Player1 is bust trun to plaer 2
            if player1points > 21:
                reward1 = -1

        # Stick and it's palyer2 turn
        elif action1 == 1:
            if player1points > 21:
                reward1 = -1
            if action2 == 0:
                game.player2.draw(game.deck)
                player2points = game.player2.calculate()
                # if player2 is bust terminate game
                if player2points > 21:
                    reward2 = -1
                    game.terminal = True

                #dealer sticks on 17 or greater
                while dealerpoints < 17:
                    game.dealer.draw(game.deck)
                    dealerpoints = game.dealer.calculate()

                # find a winner
                if dealerpoints > 21:
                    if player1points <= 21:
                        reward1 = 1
                else:
                    if player1points <= 21:
                        if player1points < dealerpoints:
                            reward1 = -1
                        elif player1points == dealerpoints:
                            reward1 = 0
                        else:
                            reward1 = 1
            elif action2 == 1:
                game.terminal = True
                    # dealer sticks on 17 or greateer
                while dealerpoints < 17:
                    game.dealer.draw(game.deck)
                    dealerpoints = game.dealer.calculate()

                # find a winner
                if dealerpoints > 21:
                    if player1points <= 21:
                        reward1 = 1
                    if player2points <= 21:
                        reward2 = 1
                else:
                    if player1points <= 21:
                        if player1points <= dealerpoints:
                            reward1 = -1
                        elif player1points == dealerpoints:
                            reward1 = 0
                        else:
                            reward = 1
                    if player2points  <= 21:
                        if player2points <= dealerpoints:
                            reward1 = -1
                        elif player2points == dealerpoints:
                            reward1 = 0
                        else:
                            reward = 1
        return player1points, player2points, dealerpoints, reward1, reward2
