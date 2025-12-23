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