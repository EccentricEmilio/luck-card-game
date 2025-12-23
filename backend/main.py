from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import pydealer
from card_utils import abbreviate
pydealer.Card.abbreviate = abbreviate   

app = FastAPI()
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.get("/")
def get_index():
    return FileResponse("../frontend/index.html")

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