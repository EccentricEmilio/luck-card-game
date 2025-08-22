class game:
  def __init__(self, player_amount, is_game=True):
    self.player_amount = player_amount
    self.is_game = is_game

  def setup(self):
    players = [
          
    ]
    pass

  def ask(self, question):
    answer = input(question)
    if answer == "exit":
      self.is_game = False
    return answer
  
  

SevenGame = game(4)

def main():
  
  while SevenGame.is_game:
    
    SevenGame.ask("Hej?")


main()