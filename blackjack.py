"""
A simplified version: Each time the game starts with a new deck of 52 cards, and is always between one dealer
and one player. The dealer should play by the rule of hitting at 16 or lower, staying at 17 or higher.
The player can only hit or stay (no split or double down). The payout for Blackjack should be 3:2

The object of the game is to beat the dealer in one of the following ways:
Get 21 points on the player's first two cards (called a "blackjack" or "natural"), without a dealer blackjack;
Reach a final score higher than the dealer without exceeding 21; or
Let the dealer draw additional cards until their hand exceeds 21 ("busted").
"""
from deck import Deck
from blackjack_player import Player

class BlackJack:
    def __init__(self,human=True):
        self.human = human
        self.player = self.create_player('player')
        self.dealer = self.create_player('Dealer')
        self.winner = None

    def create_player(self, name):
        if self.human:
            name = input("Enter {}'s name:".format(name))
        return Player(name)

    def play_game(self):
        while True:
            self.play_round()
            self.display_winner()
            choice = input("Player, Continue(Y) or Stop(N): ")
            self.empty_table()
            print('"""""""""""""""""""""""""""')
            if choice in {'N','n'}:
                break
            print()
    
    def play_round(self):
        deck = Deck()
        deck.shuffle()
        for i in range(2):
            self.player.add_card(deck.draw_card())
            self.dealer.add_card(deck.draw_card())
            self.display_card(self.player)
            self.display_card(self.dealer)
            self.player.current_score()
            self.dealer.current_score()

        while True:
            choice = input("Player {}, Hit(Y) or Stop(N): ".format(self.player))
            if choice in {'N','n'}:
                break
            self.player.add_card(deck.draw_card())   
            self.display_card(self.player)
            if self.player.current_score()>21:
                print('{} just busted!'.format(self.player))
                self.winner = self.dealer
                return
     
        if self.player.final_score == 21 and self.player.cards_in_hand() == 2:
            print('{} got blackjack!'.format(self.player))
        # For dealer, hit until total value is at least 17
        # Compare player's score with dealer's and display winner
        # In terms of a draw, it is counted as a win for the dealer
        # Soft hit not applied here
        while self.dealer.current_score()<17:
            self.dealer.add_card(deck.draw_card())
            self.display_card(self.dealer)
            if self.dealer.current_score()>21:
                print('{} just busted!'.format(self.dealer))
                self.winner = self.player
                return

        if self.dealer.final_score == 21 and self.dealer.cards_in_hand() == 2:
            print('{} got blackjack!'.format(self.dealer))
        if self.dealer.final_score == 21:
            if self.dealer.cards_in_hand()>2 and self.player.cards_in_hand()==2:
                self.winner = self.player
            else: 
                self.winner = self.dealer
        elif self.dealer.final_score>=self.player.final_score:
            self.winner = self.dealer
        else:
            self.winner = self.player

    def display_card(self, person):
        print('{} displayed card {}'.format(person, person.top_card()))
    
    def empty_table(self):
        self.player.empty_hand()
        self.dealer.empty_hand()
        self.winner = None

    def display_winner(self):
        print('{} has a total {}.'.format(self.player, self.player.current_score()))
        print('{} has a total {}.'.format(self.dealer, self.dealer.current_score()))
        print('The winner of the game is:', self.winner.name)
