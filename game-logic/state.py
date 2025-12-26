import pydealer 
from constants import *
pydealer.Card.abbreviate = abbreviate

class GameState:
    def __init__(self):
        self.TOTAL_CARDS_PER_HAND = CUSTOM_RULES["cards_per_hand"]
        self.turn_index = 0
        self.player_count = CUSTOM_RULES["player_count"]
        self.board = []
        self.current_round = {}
        self.deck = pydealer.Deck() 
        self.deck.shuffle()

        self.players = PLAYER_NAMES[0:CUSTOM_RULES["player_count"]]
        self.players_hands = {p: [] for p in self.players} 
        self.starting_player = None

    def deal_initial_hands(self):
        for hand in self.players_hands.values():
            card_stack = self.deck.deal(self.TOTAL_CARDS_PER_HAND)
            hand.extend(c.abbreviate() for c in card_stack)

    def return_turn_order(self):
        order = []
        n = len(self.players)
        current = self.starting_player
    
        for _ in range(n):
            order.append(self.players[current])
            current = (current + 1) % n
    
        return order    