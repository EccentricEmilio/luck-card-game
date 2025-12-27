from terminal_ui import TerminalUI
from state import GameState
from engine import GameEngine
import pydealer
from constants import *
pydealer.Card.abbreviate = abbreviate

players_hands_debug = {
    "Abraham": ["3C", "3D", "6C", "9C", "9D"],
    "Benjamin": ["2H", "4S", "6S", "8H", "KC"],
    "Caleb": ["2C", "JC", "KD", "KS", "QC"],
    "Daniel": ["2S", "5H", "AS", "JD", "QH"]
}

def run_terminal_game():
    state = GameState()
    engine = GameEngine(state)
    ui = TerminalUI()

    state.deal_initial_hands()
    state.debug_set_hands(players_hands_debug)  # For testing purposes
    engine.determine_starting_index()
    # Deck will contain duplicate cards if using debug hands
    ui.print_game_state(state.turn_index, state.players_hands, 
                        initial_setup=True, starting_player=state.players[state.starting_player_index])
    while not state.game_is_over:
        engine.process_turn(ui.prompt_player)
        engine.resolve_round() # determine round winner and update state
        ui.print_game_state(state.turn_index, state.players_hands)# process each player's turn
        #engine.advance_state() # prepare for next round

    engine.print_winner()
if __name__ == "__main__":
    run_terminal_game()