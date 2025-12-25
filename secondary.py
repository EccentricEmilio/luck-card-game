import pydealer
#from card_utils import abbreviate
VALUE_MAP = {
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "T",
    "Jack": "J",
    "Queen": "Q",
    "King": "K",
    "Ace": "A"
}

POKER_RANKS = {
    "values": {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
    }
}

'''
self.board = {
            "round_1" : round_1
        }
        round_1 =  {
            "winner" : "player-1",
            "player-1" : ["A"],
            "player-2" : ["3"], 
        }
'''

def abbreviate(self):
    v = VALUE_MAP[self.value]
    abbreviation = v + self.suit[0]
    return abbreviation
pydealer.Card.abbreviate = abbreviate   

class GameState:
    def __init__(self, player_count=3):
        self.TOTAL_CARDS_PER_HAND = 5
        self.turn_index = 0
        self.main_player = None
        self.active_player = "player-1"
        self.player_count = player_count
        self.board = {}
        self.deck = pydealer.Deck()
        self.deck.shuffle()

        self.players_hands = {} 
        self.players = []
        for i in range(1, player_count + 1):
            self.players_hands["player-" + str(i)] = []
            self.players.append("player-" + str(i))

    def deal_initial_hands(self):
      for i in range(1, self.player_count + 1):
        card_stack = self.deck.deal(self.TOTAL_CARDS_PER_HAND)
        cards = [c.abbreviate() for c in card_stack]
        self.players_hands["player-" + str(i)] = cards
      
      self.determine_main_player()

    def process_turn(self):
        
        pass
    
    def prompt_player(self, player):
        print("Choose which cards to play.")
        self.print_hand("This is your hand: ", self.show_hand(player))
        chosen_cards = input("Choose which cards to play: ")
        chosen_cards = chosen_cards.split()
        self.print_hand("You have chosen these cards: ", chosen_cards)
        return chosen_cards

    def show_hand(self, player_name):
      hand = self.players_hands[player_name]
      return hand
    
    def print_hand(self, prefix: str, hand: list):
      message = [prefix]
      for card in hand:
          message.append(card)
      print(" ".join(message))
        

    def print_game_state(self):
        print("------------------------")
        print("Turn: " + str(self.turn_index))
        print("Hands:")

        
        for player in self.players:
            message = [str(player), ":"]
            for card in self.show_hand(player):
                message.append(card)
            print(" ".join(message))
    
    def return_deck_size(self):
        return len(self.deck)
    
    def print_deck_size(self):
        print(str(self.return_deck_size()) + " cards left")
    


    def determine_main_player(self):
      winner = None
      winner_value = -1
      for p in self.players:
        hand = self.players_hands.get(p)
        card = hand[-1]
        value = card[0]
        rank_value = POKER_RANKS["values"].get(value)

        if rank_value >= winner_value:
           winner = p
           winner_value = rank_value
      self.main_player = winner

def game_setup(player_count: int):
    print("Starting game with", player_count, "players")
    game_state = GameState(player_count)
    game_state.deal_initial_hands()
    game_state.print_game_state()
    print(game_state.main_player + " is the main player this game!")
    return game_state



if __name__ == "__main__":
   game_state = game_setup(3)
