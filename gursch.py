import fastapi
import pydealer

def abbreviate(self):
    abbreviation = self.value[0] + self.suit[0]
    return(abbreviation)
setattr(pydealer.Card, 'abbreviate', abbreviate)


deck_1 = pydealer.Deck()
deck_1.shuffle()

app = fastapi.FastAPI()

@app.post("/ai-move")
def ai_move(state: dict):
    amount_of_cards = state["num_cards"]
    card_stack = deck_1.deal(amount_of_cards)
    card = [c.abbreviate() for c in card_stack]
    return {"play": card}
