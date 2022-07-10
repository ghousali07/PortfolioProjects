import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3,'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

# To return the String value of Card Class overriding the original method.
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)  # random.shuffle function doesn't return anything,so we don't need to return

    # Function to draw one Card from the deck.
    def draw_card(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # if there is a list of multiple cards to add in the deck we will append that list
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
            # if there is only one card to add we will append it.
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


player_one = Player('Ghous')
player_two = Player('Ahad')

new_deck = Deck()
new_deck.shuffle()

'''Each Player need to have half of the cards from the Deck so we are dealing half of the cards from the deck 
to each player '''
for i in range(26):
    player_one.add_cards(new_deck.draw_card())
    player_two.add_cards(new_deck.draw_card())


game_on = True
rounds = 0

while game_on:

    rounds += 1
    print(f'Rounds Passed {rounds}')

    if len(player_one.all_cards) == 0:
        print('Player One Lost, Player Two Won')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two Lost, Player One Won')
        game_on = False
        break

    # Adding cards at the table to start a round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:
        # using -1 with value because at every round it will draw a unique card at the end of the stack not
        # the same card that was added at the top of the stack after a round has won.
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_two_cards[-1].value < player_one_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False

        # AT WAR CONDITION
        else:
            print('WAR STARTED')

            if len(player_one.all_cards) < 5:
                print('Player 1 Loses all the Cards')
                print('Player 2 WON !')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('Player 2 Loses all the Cards')
                print('Player 1 WON !')
                game_on = False
                break

            else:
                for x in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


