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

ERROR_MESSAGES = {
            "no_cards": "No cards chosen.",
            "invalid_card": "Invalid card chosen.",
            "duplicate_cards": "Duplicate cards chosen.",
            "different_values": "All chosen cards must be of the same value.",
            "mismatched_count": "You must play the same number of cards as player-1."
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
        self.current_round = {}
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
        self.turn_index += 1
        self.current_round = {}
        for p in self.players:
            print(p + "'s turn.")
            prompt = self.prompt_player(p)
            self.current_round[p] = prompt
            print(self.currrent_round)
                
        
        
        '''
        turn_active = True
        while turn_active:
            print("It's " + self.active_player + "'s turn.")
            self.active_player = self.players[self.players.index(self.active_player) + 1]
            print("Next up: " + self.active_player)
            
            
            
            
            if self.players[-1] ==  self.active_player:
                turn_active = False
        '''
            

    def prompt_player(self, player):
        self.print_hand("This is your hand:", self.show_hand(player))
        chosen_cards = input("Choose which cards to play: ")
        chosen_cards = chosen_cards.split()
        
        invalid_input = False
        error_flags = {
            "no_cards": True if len(chosen_cards) == 0 else False,
            "invalid_card": True if any(c not in self.show_hand(player) for c in chosen_cards) else False,
            "duplicate_cards": False,
            "different_values": False,
            "mismatched_count": False
        }
        
        for key in error_flags.keys():
            if len(chosen_cards) != len(set(chosen_cards)):
                print("Duplicate cards chosen.")
                invalid_input = True

            if len(chosen_cards) != 1:
                chosen_values = [c[0] for c in chosen_cards]
                if len(chosen_values) != chosen_values.count(chosen_values[0]):
                    print("All chosen cards must be of the same value.")
                    invalid_input = True

            if player != "player-1":
                if len(chosen_cards) != self.current_round.get("player-1"):
                    print("You must play the same number of cards as player-1.")
                    invalid_input = True
            
        if invalid_input:
            return self.prompt_player(player)
        
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
        print("------------------------")
        print("Turn: " + str(self.turn_index))
        print("Hands:")

        
        for player in self.players:
            message = [str(player) + "'s hand:"]
            for card in self.show_hand(player):
                message.append(card)
            print(" ".join(message))
        
        if self.turn_index == 0:
            print("Main Player: " + str(self.main_player))
        print("------------------------")
        print("------------------------")
    
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
    return game_state



if __name__ == "__main__":
   game_state = game_setup(3)
   game_state.process_turn()