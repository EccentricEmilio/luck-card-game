from engine import GameEngine
from state import GameState


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