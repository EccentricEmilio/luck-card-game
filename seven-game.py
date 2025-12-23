class game:
  def __init__(self, player_amount, run=True):
    self.player_amount = player_amount
    self.run = run

  def setup(self):
    players = []
    for i in range(self.player_amount):
      players.append("player" + "_" + str(i+1))

    players_points = {}
    for i in players:
      players_points[i] = 0
    
  def ask(self, question):
    answer = input(question)
    if answer == "exit":
      self.is_game = False
    return answer
  
class Simulation:
  def __init__(self, game_amount=1, run=True):
    self.sim_amount = game_amount
    self.run = run

  
SevenGame = game(4)

def start_sim():
  input("How many games?")

def

def main():
  sim = Simulation()
  while SevenGame.run:
    
    SevenGame.ask("Hej: ")


if __name__ == "__main__":
  main()