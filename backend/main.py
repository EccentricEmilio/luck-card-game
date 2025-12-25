from fastapi import FastAPI, Query, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import pydealer
#from card_utils import abbreviate
VALUE_MAP = {
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8 ",
    "9": "9",
    "10": "T",
    "Jack": "J",
    "Queen": "Q",
    "King": "K",
    "Ace": "A"
}

def abbreviate(self):
    v = VALUE_MAP[self.value]
    abbreviation = v + self.suit[0]
    return abbreviation
pydealer.Card.abbreviate = abbreviate   

class GameState:
    def __init__(self, player_count=3):
        self.TOTAL_CARDS_PER_HAND = 5
        self.turn_index = 0
        self.active_player = "player-1"
        self.player_count = player_count
        self.played_cards = {}

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
    
    def return_deck_size(self):
        return len(self.deck)

app = FastAPI()
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

# Allow requests from your frontend
origins = [
    "http://127.0.0.1:5500",  # if you're serving HTML via a separate port
    "http://localhost:5500",
    "http://127.0.0.1:8000",  # optional if same port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, GET, OPTIONS etc.
    allow_headers=["*"],
)

@app.get("/")
def get_index():
    return FileResponse("../frontend/index.html")

@app.get("/start_game")
def start_game(request: Request, player_count: int = Query(3, ge=2, le=5)):
    print("Starting game with", player_count, "players")
    game_state = GameState(player_count)
    game_state.deal_initial_hands()
    return game_state.players_hands









@app.post("/ai-move")
def ai_move(state: dict):
    deck = pydealer.Deck()
    deck.shuffle()

    amount_of_cards = 5
    player_count = 3
    player_cards = {}
    for i in range(1, player_count+1):
        card_stack = deck.deal(amount_of_cards)
        card = [c.abbreviate() for c in card_stack]
        player_cards["hand-" + str(i)] = card

    return player_cards