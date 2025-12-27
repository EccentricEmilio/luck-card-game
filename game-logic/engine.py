from constants import *
from state import GameState
  
class GameEngine:
    def __init__(self, state: GameState):
        self.state = state

    def process_turn(self, prompt_player: callable):
        self.current_round = {}
        self.round_is_over = False
        
        # players = [Abraham, Benjamin, Caleb, Daniel]
        # index =   [0, 1, 2, 3]
        
        last_player_index = self.state.starting_player_index - 1
        if last_player_index < 0:
            last_player_index = len(self.state.players) - 1
        
        self.state.active_player_index = self.state.starting_player_index
        while not self.round_is_over:
            if self.state.active_player_index == last_player_index:
                self.round_is_over = True
            
            active_player = self.state.players[self.state.active_player_index]
            # Use injected callable to prompt player for printing instead of hardcoding terminal print here.
            print("It's " + active_player + "'s turn.")

            chosen_cards = prompt_player(active_player, self.state.players_hands[active_player], self.validate_player_input)
            self.state.current_round[active_player] = chosen_cards

            # Shift active player
            self.state.active_player_index += 1
            if self.state.active_player_index >= len(self.state.players):
                self.state.active_player_index = 0
                
            
        # # Old code below, kept for reference
        '''
        self.turn_index += 1
        
        for p in self.players:
            print(p + "'s turn.")
            prompt = self.prompt_player(p)
            self.current_round[p] = prompt
            print(self.current_round)
                
        
        
        
        turn_active = True
        while turn_active:
            print("It's " + self.active_player + "'s turn.")
            self.active_player = self.players[self.players.index(self.active_player) + 1]
            print("Next up: " + self.active_player)
            
            
            
            
            if self.players[-1] ==  self.active_player:
                turn_active = False
        '''

    def validate_player_input(self, player, chosen_cards):
        # normalize
        chosen_cards = [c.upper() for c in chosen_cards]
        starting_player = self.state.players[self.state.active_player_index]

        hand = [c.upper() for c in self.show_hand(player)]
        if len(chosen_cards) == 0:
            return False, ERROR_MESSAGES["no_cards"]
        if any(c not in hand for c in chosen_cards):
            return False, ERROR_MESSAGES["invalid_card"]
        if len(chosen_cards) != len(set(chosen_cards)):
            return False, ERROR_MESSAGES["duplicate_cards"]
        if player != starting_player:
            if len(chosen_cards) != len(self.state.current_round[starting_player]):
                return False, ERROR_MESSAGES["mismatched_count"]
        
        values = [c[0] for c in chosen_cards]
        if player == starting_player:
            if len(set(values)) != 1:
                return False, ERROR_MESSAGES["different_values"]
        if player != starting_player:
            if CUSTOM_RULES["response_requires_duplicates"]:
                if chosen_cards.count(values[0]) < self.state.current_round[starting_player].count(self.state.current_round[starting_player][0]):
                    return False, ERROR_MESSAGES["different_values"]

        return True, None

    def show_hand(self, player_name):
      hand = self.state.players_hands[player_name]
      return hand

    def determine_starting_index(self):
        winner = None
        winner_value = -1
        for p in self.state.players:
            hand = self.state.players_hands.get(p)
            card = hand[-1]
            value = card[0]
            rank_value = POKER_RANKS["values"].get(value)

            if rank_value >= winner_value:
               winner = p
               winner_value = rank_value
        winner_index = self.state.players.index(winner)
        self.state.starting_player_index = winner_index
        self.state.active_player_index = winner_index