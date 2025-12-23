from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import pydealer

def abbreviate(self):
    if self.value[0:2] == "10":
        abbreviation = self.value[0:2] + self.suit[0]
    else:
        abbreviation = self.value[0] + self.suit[0]
    return(abbreviation)
setattr(pydealer.Card, 'abbreviate', abbreviate)

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
    print(player_cards)

    return player_cards