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
    
# refactor below
        
class GameEngine:
    def __init__(self, state: GameState):
        self.state = state

    def process_turn(self):
        self.turn_index += 1
        self.current_round = {}
        for p in self.players:
            print(p + "'s turn.")
            prompt = self.prompt_player(p)
            self.current_round[p] = prompt
            print(self.current_round)
                
        
        
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

        valid, err = self.validate_player_input(player, chosen_cards)
        if not valid:
            print(err)
            return self.prompt_player(player)

        self.print_hand("You have chosen these cards: ", chosen_cards)
        return chosen_cards
    
    def validate_player_input(self, player, chosen_cards):
        # normalize
        chosen_cards = [c.upper() for c in chosen_cards]

        hand = [c.upper() for c in self.show_hand(player)]
        if len(chosen_cards) == 0:
            return False, ERROR_MESSAGES["no_cards"]
        if any(c not in hand for c in chosen_cards):
            return False, ERROR_MESSAGES["invalid_card"]
        if len(chosen_cards) != len(set(chosen_cards)):
            return False, ERROR_MESSAGES["duplicate_cards"]
        if player != self.main_player:
            if len(chosen_cards) != len(self.current_round[self.main_player]):
                return False, ERROR_MESSAGES["mismatched_count"]
        
        values = [c[0] for c in chosen_cards]
        if player == self.main_player:
            if len(set(values)) != 1:
                return False, ERROR_MESSAGES["different_values"]
        if player != self.main_player:
            if CUSTOM_RULES["response_requires_duplicates"]:
                if chosen_cards.count(values[0]) < self.current_round[self.main_player].count(self.current_round[self.main_player][0]):
                    return False, ERROR_MESSAGES["different_values"]

        return True, None

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
    

def game_setup():
    game_state = GameState()
    print("Starting game with", game_state.player_count, "players")
    game_state.deal_initial_hands()
    game_state.determine_main_player()
    game_state.print_game_state()
    return game_state


def run_terminal_game():
    state = GameState()
    engine = GameEngine(state)

    '''
    # Setup
    game.deal_initial_hands()
    game.determine_main_player()

    while not game.is_over():
        game.process_turn()
        game.resolve_round()
        game.advance_state()

    game.print_winner()
    '''


if __name__ == "__main__":
   pass  # run_terminal_game()
   


